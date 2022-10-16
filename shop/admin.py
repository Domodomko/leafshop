from django.contrib import admin
from .models import *
from django.db import models
from django.forms import TextInput, Textarea
from modeltranslation.admin import TranslationAdmin
from django.contrib.auth.models import Group

admin.site.unregister(Group)


class ProductToCartInline(admin.StackedInline):
    model = ProductToCart
    verbose_name = 'Product To Cart'
    verbose_name_plural = 'Products To Cart'
    extra = 0
    readonly_fields = ('product', 'quantity')
    can_delete = False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    fieldsets = (
        (None, {
            "fields": (
                'name',
            ),
        }),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name', 'category')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '40'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 8, 'cols': 80})},
    }
    fieldsets = (
        (None, {
            "fields": (
                'name',
                'category',
                'price',
                'description',
                'image'
            ),
        }),
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('id', 'is_active')
    list_display_links = ('id',)
    readonly_fields = ('is_active',)
    list_filter = ('is_active',)
    ordering = ('is_active',)
    fieldsets = (
        (None, {
            "fields": (
                'is_active',
            ),
        }),
    )

    inlines = [ProductToCartInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('id', 'shipping_first_name', 'shipping_last_name', 'created_at', 'is_active', 'is_paid')
    list_display_links = ('id', 'shipping_first_name', 'shipping_last_name')
    list_filter = ('is_active', 'is_paid', 'shipping_province')
    list_editable = ('is_paid',)
    search_fields = ('shipping_first_name',
                     'shipping_last_name',
                     'shipping_address',
                     'shipping_city',
                     'shipping_province',
                     'shipping_postal',
                     'shipping_phone',
                     'billing_first_name',
                     'billing_last_name',
                     'billing_address',
                     'billing_city',
                     'billing_province',
                     'billing_postal',
                     'billing_phone',
                     )
    ordering = ('-created_at',)
    readonly_fields = ('email',
                       'cart',
                       'created_at',
                       'shipping_first_name',
                       'shipping_last_name',
                       'shipping_address',
                       'shipping_city',
                       'shipping_province',
                       'shipping_postal',
                       'shipping_phone',
                       'billing_first_name',
                       'billing_last_name',
                       'billing_address',
                       'billing_city',
                       'billing_province',
                       'billing_postal',
                       'billing_phone',
                       'is_active',
                       )
    fieldsets = (
        ('Base Info', {
            'fields': (
                'email',
                'cart',
                'created_at',
                'is_active',
                'is_paid',)}),
        ('Shipping', {
            'fields': (
                'shipping_first_name',
                'shipping_last_name',
                'shipping_address',
                'shipping_city',
                'shipping_province',
                'shipping_postal',
                'shipping_phone',
            )}),
        ('Billing', {
            'fields': (
                'billing_first_name',
                'billing_last_name',
                'billing_address',
                'billing_city',
                'billing_province',
                'billing_postal',
                'billing_phone',
            )}),
    )


@admin.register(AboutTeaContent)
class AboutTeaContentAdmin(admin.ModelAdmin):
    model = AboutTeaContent
    list_display = ('id',)
    list_display_links = ('id',)


@admin.register(BankProps)
class BankPropsAdmin(admin.ModelAdmin):
    model = BankProps
    list_display = ('id',)
    list_display_links = ('id',)


@admin.register(ShopPolicy)
class ShopPolicyAdmin(admin.ModelAdmin):
    model = ShopPolicy
    list_display = ('id',)
    list_display_links = ('id',)
