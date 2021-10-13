from django.contrib import admin
from .models import Member, SetList, LastUpdateDT

# Register your models here.
admin.site.register(Member)
admin.site.register(SetList)
admin.site.register(LastUpdateDT)
