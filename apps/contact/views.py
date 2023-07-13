from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST, files=request.FILES)
        print(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, "your message was successfully saved")
            return redirect('.')
        messages.info(request, 'fields must not bee empty')
    ctx = {
        'form': form
    }
    return render(request, 'contact/contact.html', ctx)
