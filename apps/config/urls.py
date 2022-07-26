from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include


urlpatterns = [
    path('',
        TemplateView.as_view(template_name='home.html'),
        name='home'),
    path('', include('apps.users.urls')),

    path('admin/', admin.site.urls),
]
