from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form
from django import forms
from custom_users.models import MyUser
from services import RSA_keys_manipulate


class LoginForm(Form):
    """
        Форма для авторизации пользователя
    """
    current_user = None     # текущий пользователь

    login = forms.CharField(label='Логін',
                            max_length=32)
    public_key = forms.CharField(label='Публічний ключ',
                                 max_length=10240,
                                 widget=forms.Textarea)

    def clean_login(self):
        users = MyUser.objects.filter(login=self.cleaned_data.get('login'))

        if not users:
            raise ValidationError('Введеного логіну немає в системі')

        self.current_user = users[0]
        return users[0].login

    def clean_public_key(self):
        users = MyUser.objects.filter(login=self.cleaned_data.get('login'))

        if users:
            self.current_user = users[0]

            try:
                return self.check_pair()

            except:
                raise ValidationError('Ключ невірний')


        else:
            raise ValidationError('Ключа до неіснуючого логіну немає в системі')

    def check_pair(self):
        public_key_value = self.cleaned_data.get('public_key')
        return RSA_keys_manipulate.check_signature(public_key=public_key_value,
                                                   signature=self.current_user.signature)


class RegisterForm(ModelForm):
    """
        Форма для регистрации пользователя
    """

    class Meta:
        model = MyUser
        fields = ('login', 'private_key')
        labels = {'login': 'Логін',
                  'private_key': 'Приватний ключ'}

    public_key = forms.CharField(label='Публічний ключ',
                                 max_length=10240,
                                 widget=forms.Textarea)

    def clean_public_key(self):
        try:
            return RSA_keys_manipulate.check_keys_valid(public_key=self.cleaned_data.get('public_key'),
                                                        private_key=self.cleaned_data.get('private_key'))
        except:
            raise ValidationError('Невірна зв\'язка ключів, перевірте ключі')
