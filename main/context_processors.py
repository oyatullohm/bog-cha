import datetime
from .models import Month ,Month_cost

def create_month(request):
    user = request.user
    online_date =datetime.date.today()
    if user.is_authenticated:
        date  = str(user.date)
        date = date[:7]
        month = str(online_date)[:7]
        if date != month:
            customers = user.customers.all()
            check = 1
            for customer in customers:
                month = Month.objects.get_or_create(customer=customer,month=online_date)
                if check == 1:
                    user.date = online_date
                    user.save()
                    check +=1
        month_cost = str(Month_cost.objects.last())
        month_cost = month_cost[:7]
        if month_cost != month:
            Month_cost.objects.create()
    return {'date':online_date}
