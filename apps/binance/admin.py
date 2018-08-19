from django.contrib import admin
from .models import Market


class MarketAdmin(admin.ModelAdmin):

    list_display = ['market', 'url', 'status', 'update_date']
    list_filter = ['market']
    search_fields = ('market',)


admin.site.register(Market, MarketAdmin)
