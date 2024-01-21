from django.contrib.auth import logout
from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.contrib import messages
import datetime
from .decoratr import deco_login


from django.contrib.auth import  login ,logout, authenticate
class RegisterView(View):
    def get(self,request):
        return render(request, 'account/signup.html')
    def post(self,request):
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user =  CustomUser.objects.create_user(
                                        username=username,
                                        phone=phone,
                                        password=password,
                                        )
        if user:
            messages.success(request, " сиз Ру'йхатдан У'ттингиз ")
            return redirect('main:login')
        messages.success(request, "error")
        return  redirect('main:signup')

class LoginView(View):
    def get(self,request):
        if  request.user.is_authenticated == True:
            return redirect('main:home')
        return render (request,'account/login.html')

    def post(self,request):
        if  request.user.is_authenticated == True:
            return redirect('main:home')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            # user = authenticate(request,username=username,password=password)
            try:
                user = CustomUser.objects.get(username=username)
                if user is not None:
                    login(request,user)
                    return redirect('/')
            except:
                messages.error(request, " Логин Йоки  Парол Хато !")
                return redirect('main:login')
        return redirect('main:login')


class HomeView(View):
    @deco_login
    def get(self,request):
        user = request.user
        if user.active == True:
            customer = user.customers.all().order_by('-active')
            month = Month.objects.all().order_by('-id')
            context={'customer':customer,'month':month}
            return render(request,'index.html',context)
        return render(request,'payment.html')



class CreateCustomerView(View):
    @deco_login
    def post(self,request):
        user = request.user
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        total_summa = request.POST.get('total_summa')
        customer = Customer.objects.create(bogcha=user,name=name,phone=str(phone),total_summa=int(total_summa))
        if customer:
            messages.success(request, f"Бола К,у'шилди")
        return redirect('main:home')



class DetailCustomerView(View):
    @deco_login
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
        month_ = str(month)
        month_ = month_[:7]
        if payment > 0:
            payment =  Payment.objects.create(month=month, customer=customer, summa=payment,user=request.user)
            if online_date == month_:
                customer.summa += payment.summa
            messages.success(request, "Ту'лов Амалга ошди ")
        customer.save()
        return redirect(f'main:home')

class Pay_HistoryView(View):
    @deco_login
    def get(self,request):
        payment= Payment.objects.filter(user=request.user.id).order_by('-id').select_related('month','customer')
        return render(request,'pay-detail.html',{'payment':payment})
    @deco_login
    def post(self,request):
        summa = request.POST.get('summa')
        id = request.POST.get('id')
        payment = Payment.objects.get(id= int(id))
        payment.summa = int(summa)
        payment.save()
        return redirect('main:payment_history')

class CostView(View):
    @deco_login
    def get(self,request):
        month  = Month.objects.last()
        cost =  Cost.objects.filter(customuser=request.user,month=month).order_by('-id')
        return render(request , 'cost.html', {'cost':cost ,'month':month})
    @deco_login
    def post(self,request):
        summa = request.POST.get('pul')
        text = request.POST.get('text')
        month = Month.objects.last()
        Cost.objects.create(customuser=request.user,month=month,summa=summa,text=text)
        messages.success(request, "Чк,им  Амалга ошди ")
        return redirect('main:home')


class Cost_Payment_Summa(View):
    @deco_login
    def get(self,request):
        month_costs = []
        payment  = []
        month = Month.objects.all().order_by('-id').prefetch_related('months','month_costs')
        for i in month:
            month_costs.append(Cost.objects.filter(customuser =  request.user,month= i ))
            payment.append(Payment.objects.filter(month=i,user=request.user))
        print(payment)
        print(month_costs)
  
        return render(request,'cost-payment.html',{ 'payment':payment, 'month_costs':month_costs })



def logout_(request):
    logout(request)
    return redirect('/')

def handler_404(request,exception):
    return render(request, "404.html")

def handler_500(request):
    return render(request, "500.html")