from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


PROVINCES = (
    ('Batken', 'Batken'),
    ('Jalalabat', 'Jalalabat'),
    ('Issykkul', 'Issykkul'),
    ('Osh', 'Osh'),
    ('Talas', 'Talas'),
    ('Chui', 'Chui'),
    ('Naryn', 'Naryn'),
)


class Category(models.Model):
    name = models.CharField('Name', max_length=100, default='')

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField('Name', max_length=100, default='')
    description = models.TextField('Description', max_length=1000, default='')
    image = models.ImageField('Image', null=True, blank=True)
    price = models.FloatField('Price', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Category')

    def __str__(self):
        return self.name


class Cart(models.Model):
    is_active = models.BooleanField('Is active', default=True)

    def all_products_sum(self):
        sum = 0
        for product_to_cart in self.products_to_cart.all():
            sum += product_to_cart.products_sum()
        return float(sum)

    def all_products_quantity(self):
        return sum(product_to_cart.quantity for product_to_cart in self.products_to_cart.all())

    def __str__(self):
        return f'{self.pk}'


class ProductToCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='products_to_cart', verbose_name='Product')
    quantity = models.PositiveIntegerField('Quantity', default=0, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products_to_cart',
                             verbose_name='Cart Number')

    def products_sum(self):
        return self.quantity * self.product.price


class Order(models.Model):
    email = models.EmailField('Email',)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name='order',
                                null=True, verbose_name='Cart Number')
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    is_active = models.BooleanField("Isn't finished", default=True)
    is_paid = models.BooleanField('Is paid', default=False)
    shipping_first_name = models.CharField('First name', max_length=50, null=True, default='')
    shipping_last_name = models.CharField('Last name', max_length=50, null=True, default='')
    shipping_address = models.CharField('Address', max_length=50, null=True, default='')
    shipping_city = models.CharField('City', max_length=50, null=True, default='')
    shipping_province = models.CharField('Province', max_length=50, null=True, choices=PROVINCES)
    shipping_postal = models.CharField('Postal', max_length=50, null=True, default='')
    shipping_phone = models.CharField('Phone', max_length=50, null=True, default='')

    billing_first_name = models.CharField('First Name', max_length=50, null=True, default='')
    billing_last_name = models.CharField('Last name', max_length=50, null=True, default='')
    billing_address = models.CharField('Address', max_length=50, null=True, default='')
    billing_city = models.CharField('City', max_length=50, null=True, default='')
    billing_province = models.CharField('Province', max_length=50, null=True, default='', choices=PROVINCES)
    billing_postal = models.CharField('Postal', max_length=50, null=True, default='')
    billing_phone = models.CharField('Phone', max_length=50, null=True, default='')

    def __str__(self):
        return f'Order {self.shipping_first_name} {self.shipping_last_name}'


class AboutTeaContent(models.Model):
    about_tea = RichTextField(max_length=500000, null=True, default='')
    camelia = RichTextField(max_length=500000, null=True, default='')
    names_of_tea = RichTextField(max_length=500000, null=True, default='')
    black_tea = RichTextField(max_length=500000, null=True, default='')
    green_tea = RichTextField(max_length=500000, null=True, default='')


class BankProps(models.Model):
    bank_name = models.CharField(max_length=500, null=True, default='')
    account_number = models.CharField(max_length=500, null=True, default='')
    cardholder_name = models.CharField(max_length=500, null=True, default='')


class ShopPolicy(models.Model):
    term_of_service = RichTextField(max_length=500000, null=True, default='')
    shipping_policy = RichTextField(max_length=500000, null=True, default='')
    return_policy = RichTextField(max_length=500000, null=True, default='')
    privacy_policy = RichTextField(max_length=500000, null=True, default='')
