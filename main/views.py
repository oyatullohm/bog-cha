from django.contrib.auth import logout
from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer , CustomUser , Month , Payment
from django.contrib import messages

class HomeView(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        if user.active == True:
            customer = Customer.objects.filter(bogcha = user.id)
            context={'customer':customer}
            return render(request,'index.html',context)
        return render(request,'payment.html')



class CreateCustomerView(LoginRequiredMixin,View):
    def post(self,request):
        user = request.user
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        total_summa = request.POST.get('total_summa')
        customer = Customer.objects.create(bogcha=user,name=str(name),phone=str(phone),total_summa=int(total_summa))
        if customer:
            m =  Month.objects.create(customer=customer)
            messages.success(request, f"Bola Qo'shildi{m}")
        return redirect('main:home')



class DetailCustomerView(LoginRequiredMixin,View):
    def get(self,request,pk):
        customer = Customer.objects.get(id = int(pk))
        return render (request,'customer.html',{'customer':customer})


    def post(self,request,pk):
        name = (request.POST.get('name'))
        phone = request.POST.get('phone')
        active = request.POST.get('active')
        total_summa = request.POST.get('vznos')
        payment = int(request.POST.get('payment'))
        customer = Customer.objects.get(id = int(pk))
        month =  customer.customers.all().last()
        if customer.total_summa != total_summa :
            customer.total_summa = total_summa
            customer.save()
        if customer.name != str(name):
            customer.name=str(name)
            customer.save()
        if customer.phone != phone:
            customer.phone = phone
            customer.save()
        if active == 'on':
            active = True
        else:
            active = False
        if active != customer.active:
            customer.active = active
            customer.save()
        if payment > 0:
            Payment.objects.create(month=month,summa=payment,user=request.user)
            messages.success(request, "To'lov amalga oshdi ")
        return redirect(f'/customer/{pk}')

class Pay_HistoryView(LoginRequiredMixin,View):
    def get(self,request):
        payment = Payment.objects.filter(user=request.user.id).order_by('-id')
        return render(request,'pay-detail.html',{'payment':payment})
def logout_(request):
    logout(request)
    return redirect('/')

def handler_404(request,exception):
    return render(request, "404.html")

def handler_500(request):
    return render(request, "500.html")