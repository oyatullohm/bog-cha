
from django.contrib import admin
from django.urls import path,include
from main.views import logout_
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/logout/',logout_, name = 'logout'),
    path('accounts/', include('allauth.urls')),
    path('',include('main.urls',namespace='main'))
]
