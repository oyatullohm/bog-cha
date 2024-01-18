from django.contrib.auth import logout
from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.contrib import messages
import datetime
class HomeView(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        if user.active == True:
            customer = user.customers.all().order_by('-active')
            context={'customer':customer}
            return render(request,'index.html',context)
        return render(request,'payment.html')



class CreateCustomerView(LoginRequiredMixin,View):
    def post(self,request):
        user = request.user
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        total_summa = request.POST.get('total_summa')
        customer = Customer.objects.create(bogcha=user,name=name,phone=str(phone),total_summa=int(total_summa))
        if customer:
            messages.success(request, f"Bola Qo'shildi")
        return redirect('main:home')



class DetailCustomerView(LoginRequiredMixin,View):
    def get(self,request,pk):
        customer = Customer.objects.get(id = int(pk))
        month = Month.objects.all().order_by('-id')
        return render (request,'customer.html',{'customer':customer,'month':month})


    def post(self,request,pk):
        month = request.POST.get('month')
        month = Month.objects.get(id=int(month))
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        active = request.POST.get('active')
        total_summa = request.POST.get('vznos') 
        payment = int(request.POST.get('payment'))
        customer = Customer.objects.get(id = int(pk))
        if customer.total_summa != total_summa :
            customer.total_summa = total_summa
        if customer.name != name:
            customer.name=name
        if customer.phone != phone:
            customer.phone = phone
        if active == 'on':
            active = True
        else:
            active = False
        if active != customer.active:
            customer.active = active
        online_date =datetime.date.today()
        online_date = str(online_date)[:7]
        print(month)
        month_ = str(month)
        month_ = month_[:7]
        print(type(month_))
        if payment > 0:
            payment =  Payment.objects.create(month=month, customer=customer, summa=payment,user=request.user)
            if online_date == month_:
                customer.summa += payment.summa
            messages.success(request, "To'lov amalga oshdi ")
        customer.save()
        return redirect(f'/customer/{pk}')

class Pay_HistoryView(LoginRequiredMixin,View):
    def get(self,request):
        payment = Payment.objects.filter(user=request.user.id).order_by('-id').select_related('month','customer')
        return render(request,'pay-detail.html',{'payment':payment})
    def post(self,request):
        summa = request.POST.get('summa')
        id = request.POST.get('id')
        payment = Payment.objects.get(id= int(id))
        payment.summa = int(summa)
        payment.save()
        return redirect('main:payment_history')

class CostView(LoginRequiredMixin,View):
    def get(self,request):
        month  = Month.objects.last()
        cost =  Cost.objects.filter(customuser=request.user,month=month).order_by('-id')
        return render(request , 'cost.html', {'cost':cost ,'month':month})
    def post(self,request):
        summa = request.POST.get('pul')
        text = request.POST.get('text')
        month = Month.objects.last()
        Cost.objects.create(customuser=request.user,month=month,summa=summa,text=text)
        messages.success(request, "Chiqim  amalga oshdi ")
        return redirect('main:home')



def logout_(request):
    logout(request)
    return redirect('/')

def handler_404(request,exception):
    return render(request, "404.html")

def handler_500(request):
    return render(request, "500.html")