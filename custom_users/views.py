from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

# from custom_users.controllers import change_language
from custom_users.models import MyUser
from custom_users.forms import RegisterForm
from services import RSA_keys_manipulate
from django.utils import translation


class CreateUser(CreateView):
    model = MyUser
    template_name = 'custom_users/register.html'
    form_class = RegisterForm

    def get_context_data(self, **kwargs):
        context_data = super(CreateUser, self).get_context_data()

        context_data['public_key'], context_data['private_key'] = RSA_keys_manipulate.create_keys()

        return context_data

    def get_success_url(self):
        return reverse('file_storage:file_list')

    def form_valid(self, form):
        self.object = form.save()
        self.request.session['custom_user'] = self.object.login
        self.object.signature = RSA_keys_manipulate.create_signature(private_key=self.object.private_key)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
