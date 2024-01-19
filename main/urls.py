from django.urls import path
from .views import  * 
app_name = 'main'


urlpatterns  = [
    path('', HomeView.as_view() , name='home'),
    path('accounts/signup',RegisterView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('accounts/logout/',logout_, name = 'logout'),
    path('create/customer',CreateCustomerView.as_view(),name='create_customer'),
    path('customer/<int:pk>',DetailCustomerView.as_view(),name='customer'),
    path('payment/history',Pay_HistoryView.as_view(),name='payment_history'),
    path('cost',CostView.as_view(),name='cost'),
]