from django.db import models
from django.contrib.postgres.fields import JSONField


class Basic(models.Model):

    STATUS = (
        ('AC', 'A'),
        ('DC', 'D'),
    )

    description = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS, default='AC')

    class Meta:
        abstract = True


class Market(Basic):

    market = models.CharField(max_length=255, null=False, blank=False, unique=True)
    url = models.URLField(null=True, blank=True)
    ping = JSONField(null=True, blank=True)
    server_time = JSONField(null=True, blank=True)
    system_status = JSONField(null=True, blank=True)
    exchange_info = JSONField(null=True, blank=True)
    all_tickers = JSONField(null=True, blank=True)
    orderbook_tickers = JSONField(null=True, blank=True)

    class Meta:
        verbose_name = 'Market'
        verbose_name_plural = 'Markets'

    def __str__(self):
        return self.market

    def save(self, *args, **kwargs):
        self.market = self.market.lower()
        return super(Market, self).save(*args, **kwargs)
