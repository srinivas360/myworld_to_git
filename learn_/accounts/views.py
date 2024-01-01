from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        print('---at post start srinivas-check')
        form = UserCreationForm(request.POST)
        print('--before valide fun srinivas-check', form.is_valid())
        if form.is_valid():
            print('--insdied isvalid srinivas-check')
            user = form.save()
            # log the user
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

def login_view(request):
    print('--request type', request.method, '--req', request )
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            next = request.POST.get('next')
            if next:
                return redirect(next)
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', { 'form': form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')