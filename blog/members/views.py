from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import UserRegisterForm, UserUpdateDataForm
from django.contrib.auth import views as auth_views
from blog.models import Profile,Post
from .forms import UserUpdateForm, UserCreateProfilePageForm

class CreateUser(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UpdateUserInfo(UpdateView):
    form_class = UserUpdateDataForm
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy('main')

    def get_object(self):
        return self.request.user

class ChangePassword(auth_views.PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('main')

class AuthorInfo(DetailView):
    model=Profile
    template_name = 'registration/user_info.html'

    def get_context_data(self, *args, **kwargs):
        context=super(AuthorInfo,self).get_context_data(*args,**kwargs)
        user_info=get_object_or_404(Profile,id=self.kwargs['pk'])
        context["user_info"]=user_info
        return context

class UpdateUserProfile(UpdateView):
    model=Profile
    form_class = UserUpdateForm
    template_name = 'registration/update_user_profile.html'
    success_url = reverse_lazy('main')

class CreateUserProfile(CreateView):
    model=Profile
    form_class = UserCreateProfilePageForm
    template_name = 'registration/create_user_profile.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

