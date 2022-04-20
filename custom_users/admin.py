
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from custom_users.models import MyUser
from services import RSA_keys_manipulate


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    public_key = forms.CharField(label='Public Key',
                                  max_length=10240,
                                  widget=forms.Textarea)

    class Meta:
        model = MyUser
        fields = ('login', 'private_key')

    def clean_private_key(self):
        private_key = self.cleaned_data.get("private_key")
        public_key = self.cleaned_data.get("public_key")

        if public_key and private_key:
            self.cleaned_data['signature'] = RSA_keys_manipulate.create_signature(private_key)

        else:
            raise ValidationError('Введите публичный ключ и приватный ключ')

        return private_key

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        # user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        else:
            user.signature = RSA_keys_manipulate.create_signature(self.cleaned_data.get('private_key'))

        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('login', 'is_active', 'is_admin')


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    readonly_fields = ['signature']
    list_display = ('login', 'private_key', 'signature', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('login', 'private_key', 'signature')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'public_key', 'signature', 'private_key'),
        }),
    )
    search_fields = ('login',)
    ordering = ('login',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
