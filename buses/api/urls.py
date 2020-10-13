from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from buses.api import views

urlpatterns = [
    path('drivers/api/', views.DriverList.as_view()),
    path('drivers/api/<int:pk>/', views.DriverDetail.as_view()),
    path('routes/api/', views.RouteList.as_view()),
    path('routes/api/<int:pk>/', views.RouteDetail.as_view()),
    path('buses/api/', views.BusList.as_view()),
    path('buses/api/<int:pk>/', views.BusDetail.as_view()),
    path('passengers/api/', views.PassengerList.as_view()),
    path('passengers/api/<int:pk>/', views.PassengerDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)