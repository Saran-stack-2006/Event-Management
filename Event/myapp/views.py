from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Booking
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})


def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('login')
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def add_event(request):
    if request.method == 'POST':
        Event.objects.create(
            name=request.POST['name'],
            date=request.POST['date'],
            location=request.POST['location'],
            description=request.POST['description'],
            image=request.FILES['image']
        )
        return redirect('home')
    return render(request, 'add_event.html')


@login_required(login_url='login')
def book_event(request, id):
    event = get_object_or_404(Event, id=id)
    Booking.objects.create(user=request.user, event=event)
    return redirect('my_bookings')


@login_required(login_url='login')
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings.html', {'bookings': bookings})