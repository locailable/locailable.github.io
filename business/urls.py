from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('business/', views.business, name='business'),
    path('business/<int:business_id>/', views.business_detail, name='business_detail'),
    path('business/create/', views.create_business, name='create_business'),
    path('business/update/<int:business_id>/', views.update_business, name='update_business'),
    path('business/delete/<int:business_id>/', views.delete_business, name='delete_business'),
    path('business/availability/<int:business_id>/', views.create_availability, name='create_availability'),
    path('business/review/<int:business_id>/', views.create_review, name='create_review'),
]