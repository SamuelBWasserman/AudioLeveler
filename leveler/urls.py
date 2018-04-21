from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('leveler_app/', include('leveler_app.urls')),
    path('admin/', admin.site.urls),
]