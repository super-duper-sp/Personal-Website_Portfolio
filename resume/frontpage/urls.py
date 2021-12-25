from django.urls import path
from . import views

urlpatterns = [
    path('',views.landingpage, name="landingpage"),
    path('frontpage/', views.frontpage, name="frontpage")
]
