from django.urls import path
from professionals import views


urlpatterns = [
    path('register_professional/', views.register_professional, name='register_professional' ),
    path('list_professional/', views.list_professional, name='list_professional'),
    path('detail_professional/<int:pk>/', views.detail_professional, name='detail_professional'),
    path('delete_professional/<int:pk>/', views.delete_professional, name='delete_professional'),
]