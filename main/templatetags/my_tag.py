from django import template
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

