from django.contrib import admin
from .models import *


# Категория
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


# Товар
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug',)
    ordering = ('title',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ProducerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'country',)
    search_fields = ('title',)


class Detail(admin.TabularInline):
    model = OrderDetail
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        ((u'Customer',),
         {'fields': ('name', 'phone')}),
        ((u'Order',),
         {'fields': ('total_price', 'discount', )}),
        ((u'Shipping',),
         {'fields': ('status', 'ship_to', 'comment')})
        )
    list_display = ('name', 'phone', 'status', 'total_price', 'discount', 'registered')
    search_fields = ('name', 'status')
    inlines = [Detail]


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    ordering = ('order',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Order, OrderAdmin)
#admin.site.register(OrderDetail, OrderDetailAdmin)

