from django.contrib import admin
from .models import Market, AllTickerParseExample


class MarketAdmin(admin.ModelAdmin):

    list_display = ['market', 'url', 'status', 'update_date']
    list_filter = ['market']
    search_fields = ('market',)


class AllTickerParseExampleAdmin(admin.ModelAdmin):

    list_display = ['symbol', 'price']
    search_fields = ('symbol',)


admin.site.register(Market, MarketAdmin)
admin.site.register(AllTickerParseExample, AllTickerParseExampleAdmin)
