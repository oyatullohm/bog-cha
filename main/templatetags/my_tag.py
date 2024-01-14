from django import template
register = template.Library()
@register.simple_tag
def payment_summa (summa):
    total_summa = 0
    for i in summa:
        total_summa += i.summa
    return  total_summa


@register.simple_tag
def total_summa_(objects):
    summa = 0
    for c in objects:
        x = c.customers.all().last().months.all()
        for i in x:
            summa += i.summa
    return summa

@register.simple_tag
def payment_True_or_False(summa,payment_summa):
    total_summa = 0
    for i in payment_summa:
        total_summa += i.summa
    if summa <= total_summa:
        return "✅"
    if total_summa == 0:
        return '❌'
    if total_summa > 0 and total_summa < summa:
        return '🟨'


@register.simple_tag
def total_cost(s):
    summa = 0
    for i in s:
        summa += i.summa
    return summa

