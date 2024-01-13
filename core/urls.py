
from django.contrib import admin
from django.urls import path,include , re_path
from django.conf import settings
from django.views.static import serve as mediaserve

from django.conf.urls import handler404,handler500
# from main.views import handler_404,handler_500
from main.views import logout_
from .views import RegisterView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup',RegisterView.as_view(),name='singup'),
    path('accounts/logout/',logout_, name = 'logout'),
    path('accounts/', include('allauth.urls')),
    path('',include('main.urls',namespace='main'))
]
urlpatterns += [

        re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$', mediaserve, {'document_root': settings.STATIC_ROOT}),
    ]

# handler404=handler_404
# handler500=handler_500