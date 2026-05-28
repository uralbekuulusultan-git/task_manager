from django.urls import path

from . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
