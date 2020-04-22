from django.urls import path, include
from . import views
urlpatterns = [
    path('contact', views.ContactAdd.as_view() , name='contact'),
]
