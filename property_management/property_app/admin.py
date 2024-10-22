from django.contrib import admin
from property_app.models import Property,Unit,Tenant,Lease
# Register your models here.
admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(Lease)



