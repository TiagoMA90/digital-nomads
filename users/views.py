# Imports
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .forms import UserUpdateForm
from .forms import ProfileUpdateForm
from .models import Profile
from django.contrib.auth import logout


# Function to create and save a User account
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('register_complete')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
# Function to update a User profile
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(
                request.POST, request.FILES, instance=request.user.profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)

        # If the profile and user forms are valid, save both forms
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'profile_form': profile_form,
        'user_form': user_form
    }

    return render(request, 'users/profile.html', context)


@login_required
# Function to delete a User profile
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        profile = user.profile
        profile.delete()
        user.delete()
        logout(request)
        return redirect('deregister_complete')

    return render(request, 'users/deregister.html')


def deregister_complete(request):
    return render(request, 'users/deregister_complete.html')

def register_complete(request):
    return render(request, 'users/register_complete.html')