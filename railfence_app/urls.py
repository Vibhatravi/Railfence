from django.urls import path
from . import views

urlpatterns = [
    path('', views.railfence_home, name='railfence_home'),
    path('encrypt/', views.railfence_encrypt, name='railfence_encrypt'),
    path('decrypt/', views.railfence_decrypt, name='railfence_decrypt'),
]
