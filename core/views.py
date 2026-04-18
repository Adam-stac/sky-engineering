from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from .models import Department, EngineeringTeam, User, CodeRepository


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'core/login.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Please fix the errors below')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    context = {
        'total_departments': Department.objects.count(),
        'total_teams': EngineeringTeam.objects.count(),
        'total_users': User.objects.count(),
        'total_repos': CodeRepository.objects.count(),
        'recent_teams': EngineeringTeam.objects.select_related(
            'department', 'manager'
        ).order_by('-creation_date')[:5],
    }
    return render(request, 'core/dashboard.html', context)