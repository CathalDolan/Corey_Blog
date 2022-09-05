from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Saves the form to the DB
            form.save()
            username = form.cleaned_data.get('username')
            # The "success" tag is imported into base.html in the messages class
            # f string used to add the message text content in this case
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Login Required is a decorator to ensure the User can't access profile page without being logged in
@login_required
def profile(request):
    if request.method == 'POST':
        # request.POST passes in the POST data
        # Adding the Instances populates the form with current data as opposed to the fields being blank.
        u_form = UserUpdateForm(request.POST, 
                                instance=request.user)
        # request.FILES refers to the image being uplodaded by the User
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
