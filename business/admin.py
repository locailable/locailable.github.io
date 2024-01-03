from django.contrib import admin

# Register your models here.
from .models import Business, BusinessOwner, Availability, Review

admin.site.register(Business)
admin.site.register(BusinessOwner)
admin.site.register(Availability)
admin.site.register(Review)