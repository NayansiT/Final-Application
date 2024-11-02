from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from .models import Application
from django.contrib.auth.forms import UserCreationForm
from django.utils.dateparse import parse_date

# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Registration failed. Please check the information provided.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

# Apply view to submit applications
@login_required
def apply(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, "Thank you for applying!")
            return redirect('view_status')
    else:
        form = ApplicationForm()
    return render(request, 'apply.html', {'form': form})

# Dashboard view with options for New Application and View Status
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# View Status page showing application status with exact submission date and time
@login_required
def view_status(request):
    if request.method == "POST":
        username = request.POST.get('username')
        dob = parse_date(request.POST.get('dob'))
        email = request.POST.get('email')

        applications = Application.objects.filter(name=username, date_of_birth=dob , email=email)
        if applications.exists():
            last_application = applications.last()
            context = {
                'application_status': last_application.status,
                'submission_time': last_application.submission_time,
                'name': last_application.name
            }
        else:
            messages.error(request, "No applications found for the provided details.")
            context = {'application_status': None}
    else:
        context = {}

    return render(request, 'view_status.html', context)
