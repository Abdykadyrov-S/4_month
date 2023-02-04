from django.shortcuts import render

from users.forms import UserRegisterForm


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import generic

# def register(request):
#     if request.method == "POST":
#         user_form = UserRegisterForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data["password"])
#             new_user.save()
#             return render(request, "registration/register_done.html", {"user": new_user})
#     else:
#         user_form = UserRegisterForm()
#     return render(request, "registration/register.html", {"form": user_form})



class RegisterView(generic.CreateView):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return render(request,"registration/register_done.html", {"user": new_user})
        else:
            return render(request, "registration/register.html", {"form": form})

    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/register.html", {"form": form})