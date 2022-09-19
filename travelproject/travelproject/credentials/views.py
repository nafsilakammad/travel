from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        user = request.POST['username']
        first = request.POST['firstname']
        last = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['psw']
        rpass = request.POST['psw-repeat']
        if password == rpass:
            if User.objects.filter(username=user).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user, password=password, first_name=first, last_name=last,
                                                email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'password not created')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')
