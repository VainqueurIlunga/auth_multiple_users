from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from . import forms

from business_app.views import business
from customer.views import customer
from public.views import public


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('login')


class LoginView(View):
    form_class = forms.LoginForm
    template_name = 'authentication/login.html'

    def get(self, request):
        form = self.form_class
        message = ''
        return render(
            request, self.template_name, context={'form': form, 'message': message}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                if user.is_business:
                    return redirect('business')

                if user.is_customer:
                    return redirect('customer')

                else:
                    return redirect('public')

        else:
            message = ' Mot de passe incorrecte'

        return render(
            request, self.template_name, context={'form': form, 'message': message}

        )


class RegisterView(View):
    form_class = forms.RegistrationForm
    template_name = 'authentication/register.html'

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(
            request, self.template_name, context={'form': form}
        )

    def post(self, request):
        form = forms.RegistrationForm(request.POST)
        message = ''
        if form.is_valid:
            user=form.save()
            login(request,user)
            return redirect('login')
        return render(
            request, self.template_name, context={'form': form, 'message': message}
        )
