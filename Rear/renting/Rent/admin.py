from django.contrib import admin
from Rent.models import *
# Register your models here.

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ["title","mold",'addr','size','orientation']

    def save_model(self, request, obj, form, change):
        obj.create = request.user
        super().save_model(request,obj,form,change)

admin.site.register(User)
