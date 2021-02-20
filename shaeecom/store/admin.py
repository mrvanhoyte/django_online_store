from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *

admin.site.register(Customer)
admin.site.register(Product)

admin.site.register(Order)

admin.site.register(OrderItem)
admin.site.register(ShippingAddress)



