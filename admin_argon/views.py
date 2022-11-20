from django.shortcuts import render, redirect
from admin_argon.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.contrib.auth import logout

# Create your views here.

def index(request):
  return render(request, 'pages/dashboard.html')

def billing(request):
  return render(request, 'pages/billing.html')

def profile(request):
  return render(request, 'pages/profile.html')

def tables(request):
  return render(request, 'pages/tables.html')

def rtl(request):
  return render(request, 'pages/rtl.html')

def vr(request):
  return render(request, 'pages/virtual-reality.html')

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print("Account created successfully!")
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()

  context = { 'form': form }
  return render(request, 'accounts/sign-up.html', context)


class UserLoginView(LoginView):
  template_name = 'accounts/sign-in.html'
  form_class = LoginForm


class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login/')