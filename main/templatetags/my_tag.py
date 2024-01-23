from django.core.cache import cache
from django import template
from main.models import Payment
register = template.Library()
@register.simple_tag
def total_summa_(objects):
    summa = 0
    for c in objects:
        summa += c.summa
    return summa

@register.simple_tag
def payment_True_or_False(summa,payment_summa):
    if summa <= payment_summa:
        return "✅"
    if payment_summa == 0:
        return '❌'
    if payment_summa > 0 and  payment_summa < summa:
        return '🟨'


@register.simple_tag
def total_cost(s):
    summa = 0
    for i in s:
        summa += i.summa
    return summa


@register.simple_tag
def total_cost_summa(request , i ):
    summa = 0
    user = request.user
    cost =  user.costs.filter(month=i)
    for i in cost:
        summa += i.summa
    return summa


from django.views.decorators.cache import cache_page
@cache_page(60 * 15)
@register.simple_tag
def total_payment_summa(request , i ):
    user = request.user
    summa = 0
    payment  =  Payment.objects.filter(month=i,user=user)
    for i in payment:
        summa += i.summa
    return summa

