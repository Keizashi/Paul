from django.contrib import admin
from .models import *

class SubscriberAdmin (admin.ModelAdmin):
    #list_display = ["name", "email"]
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ('name',)
    fields = ["email"]
    search_fields = ['name', 'email']
    # exclude = ["email"]
    # inlines = [FieldMappingInline]
    # fields = []
    # #exclude = ["type"]
    # #list_filter = ('report_data',)
    # search_fields = ['category', 'subCategory', 'suggestKeybord']

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)
# Register your models here.
