from django.urls import path, include

appname='accounts'
urlpatterns = [
    path('',include('django.contrib.auth.urls')),
]