from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            login = userform.cleaned_data["cardNumber"]
            password = userform.cleaned_data["password"]
            return HttpResponse("<h2>Card number : {0} |  Password : {1}</h2>".format(login, password))
        else:
            return HttpResponse("Incorrect")
    else:
        userform = UserForm()
        return render(request, "main/index.html", {"form": userform})
