from django.shortcuts import render


def login_user(request):
    ctx = {

    }
    return render(request, 'accouns/login.html', ctx)


def register(request):
    ctx = {

    }
    return render(request, 'accouns/sin-up.html', ctx)


def candidate(request):
    ctx = {

    }
    return render(request, 'accouns/candidate.html', ctx)
