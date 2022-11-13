from django.contrib import admin
from .models import Appointment, Contact, Newsletter, Quote


class AppointmentAdmin(admin.ModelAdmin):
    """
    This class is for displaying appointment in administration
    """
    date_hierarchy = 'created_date'
    list_display = ('name', 'department', 'email')
    list_filter = ('department',)
    search_fields = ('name', 'message', 'department')


class ContactAdmin(admin.ModelAdmin):
    """
    This class is for displaying contact in administration
    """
    date_hierarchy = 'created_date'
    list_display = ('name', 'email')
    list_filter = ('email',)
    search_fields = ('name', 'message')


class QuoteAdmin(admin.ModelAdmin):
    """
    This class is for displaying quote in administration
    """
    list_display = ('name', 'email', 'website')
    list_filter = ('name', 'website')
    search_fields = ('name', 'website')

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Newsletter)
