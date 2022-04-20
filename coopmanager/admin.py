from django.contrib import admin

from .models import *

admin.site.register(CoopItem)
admin.site.register(ItemType)
admin.site.register(QuantityUnit)
admin.site.register(PriceBracket)
