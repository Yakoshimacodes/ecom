from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Slider)
admin.site.register(Ad)
admin.site.register(Product)
admin.site.register(Feedback)
admin.site.register(ContactInfo)