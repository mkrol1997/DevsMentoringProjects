from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView


class UserLoginView(LoginView):
    template_name = 'users/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in!')
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_joined'] = self.request.user.date_joined.strftime('%m/%d/%Y')
        return context


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

    def get_success_url(self):
        return reverse('login')
