from django.views import View
from django.shortcuts import render , redirect
from main.models import Customer
from django.contrib import messages
class RegisterView(View):
    def post(self,request):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user =  Customer.create_user(username=username,
                                 last_name=last_name,
                                 first_name=first_name,
                                 email=email,phone=phone,
                                 password=password)
        if user:
            messages.success(request, "siz ro'yhatdan o'ttingiz")
            return redirect('/')
        messages.success(request, "error")
        return  redirect('/')