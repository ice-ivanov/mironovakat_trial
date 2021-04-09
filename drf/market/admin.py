from django.contrib import admin
from .models import Animal, Lot, Bid


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'breed', 'owner')
    fields = ('id', 'name', 'breed', 'owner')
    readonly_fields = ('id',)


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal', 'price', 'owner', 'winner_id')
    fields = ('id', 'animal', 'price', 'owner', 'winner_id')
    readonly_fields = ('id',)


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('id', 'lot', 'value', 'owner')
    fields = ('id', 'lot', 'value', 'owner')
    readonly_fields = ('id',)
