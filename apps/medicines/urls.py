from django.urls import path

from . import views

app_name = 'medicines'

urlpatterns = [
    path('', views.ListCreateView.as_view(), name='list'),
    path('<pk>/', views.EditView.as_view(), name='detail'),
    path('<pk>/delete/', views.DeleteView.as_view(), name='delete'),
]
