from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import json

# New class that is used in the HTML for the django form and to organize the data, similar to classes in C++ 
class NewUser(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-Mail', 'style': 'width: 300px;', 'class': 'form-control'}), min_length=10, max_length=50)
    firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 300px;', 'class': 'form-control'}), min_length=2, max_length=20)
    lastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 300px;', 'class': 'form-control'}), min_length=2, max_length=20)
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}), min_length=10)


#users = []

#Create your views here.
def index(request):
    if "users" not in request.session:
       request.session["users"] = []

    return render(request, "househub/home.html", {
        "users": request.session["users"]
    })

# Function that displays a blank form for GET and adds the user to the databaase if it is POST
def sign_up(request):
    if request.method == "POST":
        user = NewUser(request.POST)
        # Checks if the user input is valid
        if user.is_valid():
            # New variables for the valid input that we will send to the database
            email = user.cleaned_data["email"]
            # Need to add a check if there is already an email like the one submited so the rest of the code does not go on
            firstName = user.cleaned_data["firstName"]
            lastName = user.cleaned_data["lastName"]
            password = user.cleaned_data["password"]
            # Need to add database addition of the new user here
            # Redirect the user to the sign in page and have them log in
            #return HttpResponseRedirect(reverse("househub:login"))
            #users.append(user)
            request.session["users"] += [{"email": email, "firstName": firstName, "lastName": lastName, "password": password}]
        else:
            return render(request, "househub/sign_up.html", {
                "form": user
            })
    # Blank form
    return render(request, "househub/sign_up.html", {
        "form": NewUser()
    })
