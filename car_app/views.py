
from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import DetailView
from django.urls import reverse_lazy

# Create your views here.

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            register_form = forms.RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                return redirect('user_login')
        else:
            register_form = forms.RegisterForm()
        return render(request,'register.html', {'form': register_form, 'type': 'Registration'})
    else:
        return redirect('homepage')


class user_login(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy("homepage")

    def form_valid(self, form):
        messages.success(self.request, "Login successful")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
    
@login_required
def profile(request):
    data = User.objects.filter(username=request.user)
    return render(request, 'profile.html', {'data': data})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = forms.ChangeUserData(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('homepage')
    else:
        form = forms.ChangeUserData(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form, 'type' : 'Profile Edit'})


class pass_change(PasswordChangeView):
    template_name = 'pass_change.html'
    success_url = reverse_lazy('homepage')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


    def form_valid(self, form):
        # form.save()
        messages.success(self.request, "Password changed successfully")
        return super().form_valid(form)

    
    
class DetailCarView(DetailView):
    model = models.CarModel
    template_name = 'car_detail.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            comment_form = forms.CommentForm(data=self.request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.car = self.get_object()
                new_comment.save()
                return self.get(request, *args, **kwargs)
            else:
                return self.get(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        context['car'] = car
        context['comment_form'] = comment_form
        context['comments'] = comments
        return context
    
    
    
# class UserLogoutView(LogoutView):
#     success_url_allowed_hosts = set('user_login')

@login_required
def user_logout(request):
    messages.success(request, 'Logged out successfully')
    logout(request)
    return redirect('homepage')
    



