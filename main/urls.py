from django.urls import path
from .views import HomeView ,CreateCustomerView ,DetailCustomerView ,Pay_HistoryView
app_name = 'main'


urlpatterns  = [
    path('', HomeView.as_view() , name='home'),
    path('create/customer',CreateCustomerView.as_view(),name='create_customer'),
    path('customer/<int:pk>',DetailCustomerView.as_view(),name='customer'),
    path('payment/history',Pay_HistoryView.as_view(),name='payment_history'),
]