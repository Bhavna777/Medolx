
from django.contrib import admin
from .models import Doctor, Patient, Product, Blog, Contact, Message
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)




admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Message)
