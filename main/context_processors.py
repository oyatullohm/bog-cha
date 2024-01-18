import datetime
from .models import Month

def create_month(request):
    user = request.user
    online_date =datetime.date.today()
    if user.is_authenticated:
        date  = str(user.date)
        date = date[:7]
        month = str(online_date)[:7]
        if date != month:
            month = Month.objects.create()
            if month:
                for i in user.customers.all():
                    i.summa = 0
                    i.save()
            user.date = online_date
            user.save()
    return {'date':online_date}
