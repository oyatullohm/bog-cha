import datetime
from .models import Month , CustomUser , Customer

def create_month(request):
    user = request.user
    online_date =datetime.date.today()
    if user.is_authenticated:
        date  = str(user.date)
        date = date[:7]
        month = str(online_date)[:7]
        if date != month:
            month = Month.objects.create()
            for i in CustomUser.objects.all():
                i.date = online_date
                i.save()
            for i in Customer.objects.all():
                i.summa = 0
                i.save()
    return {'date':online_date}