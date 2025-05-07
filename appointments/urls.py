from django.urls import path
from appointments import views


urlpatterns = [
    path('register_appointment/', views.register_appointment, name='register_appointment' ),
    path('list_appointments/', views.list_appointments, name='list_appointments'),
    path('detail_appointment/<int:pk>/', views.detail_appointment, name='detail_appointment'),
    path('delete_appointment/<int:pk>/', views.delete_appointment, name='delete_appointment'),
]