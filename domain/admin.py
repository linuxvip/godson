from django.contrib import admin
from .models import domain


class DomainAdmin(admin.ModelAdmin):
    list_display = [
        'domain_name',
        'ip',
        'add_area',
        'env',
        'usage',
        ]


admin.site.register(domain, DomainAdmin)

