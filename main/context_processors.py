import datetime
from .models import Month

def create_month(request):
    user = request.user
    online_date =datetime.date.today()
    if user.is_authenticated:
        print('user login qilgan ')
        date  = str(user.date)
        date = date[:7]
        month = str(online_date)[:7]
        print(date,'date',month,'month')
        if date != month:
            print("oylar != emais ")
            customers = user.customers.all()
            check = 1
            for customer in customers:
                month = Month.objects.get_or_create(customer=customer,month=online_date)
                print(month,'bu oy')
                if check == 1:
                    user.date = online_date
                    user.save()
                    check +=1
    return {'date':online_date}
