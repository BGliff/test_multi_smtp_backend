from django.urls import path

from smtp import views

urlpatterns = [
    path('send_mail', views.send_email)
]
