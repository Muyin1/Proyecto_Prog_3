from django.urls import path
from profesor  import views

urlpatterns = [
    path('', views.profesor_list, name='profesor_list'),
    path('nuevo/', views.profesor_create, name='profesor_create'),
    path('editar/<int:pk>/', views.profesor_update, name='profesor_update'),
    path('eliminar/<int:pk>/', views.profesor_delete, name='profesor_delete'),
]
