from django.urls import path
from .views import pages, screen, ticket, about, operator, registration, probe


app_name = 'queue_app'
urlpatterns = [
    path('', screen, name='screen'),
    path('pages/', pages, name='pages'),
    path('ticket/', ticket, name='ticket'),
    path('registration/', registration, name='registration'),
    path('operator/', operator, name='operator'),
    path('about/', about, name='about'),
    path('probe/', probe, name='probe'),
   ]
