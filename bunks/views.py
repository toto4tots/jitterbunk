from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from bunks.models import Bunk
from django import forms

class NewBunkForm(forms.Form):
    to_user = forms.CharField(label="To")
    from_user = forms.CharField(label="From")

def index(request):
    User = get_user_model()
    all_users = User.objects.all()
    all_bunks = Bunk.objects.all().order_by('-time')
    return render(request, 'bunks/index.html', {'users': all_users, 'bunks': all_bunks})

def profile(request, user_id):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_id)
    bunked_user = Bunk.objects.filter(to_user=user).order_by('-time')
    user_bunked = Bunk.objects.filter(from_user=user).order_by('-time')
    return render(request, 'bunks/profile.html', {'user': user, 'bunked_user': bunked_user, 'user_bunked': user_bunked})

def bunk(request):
    User = get_user_model()
    if request.method == "POST":
        form = NewBunkForm(request.POST)
        if form.is_valid():
            cleaned_form = form.cleaned_data
            to_user_username = cleaned_form["to_user"]
            from_user_username = cleaned_form["from_user"]
            to_user = get_object_or_404(User, username=to_user_username)
            from_user = get_object_or_404(User, username=from_user_username)
            b = Bunk(to_user=to_user, from_user=from_user)
            b.save()

    return render(request, 'bunks/bunk.html', {
        "form": NewBunkForm()
    })