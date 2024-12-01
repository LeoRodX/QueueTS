from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('queue_app/', include('queue_app.urls')),
    path('', admin.site.urls),
]
