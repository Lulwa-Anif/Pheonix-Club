from django.urls import path
from club import views as clubViews

urlpatterns=[
    path('contact/us/',clubViews.ContactUsView,name='contact_us'),
    path('home/',clubViews.Home,name='home'),
    path('about/',clubViews.About,name='about'),
    path('events/',clubViews.Events,name='events'),
    path('gallery/',clubViews.Gallery,name='gallery'),
]