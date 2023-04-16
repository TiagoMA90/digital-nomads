from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .forms import UserUpdateForm
from .forms import ProfileUpdateForm

# Function to create and save a User account
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, f'{username} has been successfully created!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Decorator for Users to be required to log in and display the User profile
@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        user_form = UserUpdateForm(request.POST, instance = request.user)

        # If the profile and user forms are valid, save both forms, execute the following message and redirect/refresh the profile
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.info(request, f'Account details have been updated.')
            return redirect('profile')
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        user_form = UserUpdateForm(instance=request.user)


    context = {
        'profile_form': profile_form, 
        'user_form': user_form
    }

    return render(request, 'users/profile.html', context)
