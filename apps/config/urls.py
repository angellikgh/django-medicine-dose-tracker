from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

from apps.medicines.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('', include('apps.users.urls')),
    path('medicines/', include('apps.medicines.urls')),

    path('admin/', admin.site.urls),
]
