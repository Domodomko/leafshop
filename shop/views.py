from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    UpdateView,
    TemplateView,
    FormView,
    DeleteView,
)
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist

import json
import threading

from .models import *
from .forms import OrderShippingForm, OrderPaymentForm


# Functions
def run_in_thread(fn):
    def run(*args, **kwargs):
        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        t.start()
    return run


@run_in_thread
def email_thread(msg):
    send_mail('New Order', msg, settings.EMAIL_HOST_USER, [settings.CONTACT_US_EMAIL])


# Views
def main_page(request):
    if cart_pk := request.session.get('cart_id', False):
        try:
            cart = Cart.objects.get(pk=cart_pk)
        except ObjectDoesNotExist:
            cart = None
        if cart is None:
            cart = Cart.objects.create(is_active=True)
            cart.save()
            request.session['cart_id'] = cart.pk
    else:
        cart = Cart.objects.create(is_active=True)
        cart.save()
        request.session['cart_id'] = cart.pk
    return render(request, 'main_page.html', {'is_main_page': True, 'products': Product.objects.all(), 'categories': Category.objects.all(), 'cart': cart, 'about_tea': AboutTeaContent.objects.first()})


def cart(request):
    if cart_pk := request.session.get('cart_id', False):
        try:
            cart = Cart.objects.get(pk=cart_pk)
        except ObjectDoesNotExist:
            cart = None
        if cart is None:
            cart = Cart.objects.create(is_active=True)
            cart.save()
            request.session['cart_id'] = cart.pk
    else:
        cart = Cart.objects.create(is_active=True)
        cart.save()
        request.session['cart_id'] = cart.pk
    return render(request, 'cart_page.html', {'cart': cart})


def shop_policy(request):
    if cart_pk := request.session.get('cart_id', False):
        try:
            cart = Cart.objects.get(pk=cart_pk)
        except ObjectDoesNotExist:
            cart = None
        if cart is None:
            cart = Cart.objects.create(is_active=True)
            cart.save()
            request.session['cart_id'] = cart.pk
    else:
        cart = Cart.objects.create(is_active=True)
        cart.save()
        request.session['cart_id'] = cart.pk
    return render(request, 'shop_policy.html', {'cart': cart, 'shop_policy': ShopPolicy.objects.first()})


def about_tea(request):
    if cart_pk := request.session.get('cart_id', False):
        try:
            cart = Cart.objects.get(pk=cart_pk)
        except ObjectDoesNotExist:
            cart = None
        if cart is None:
            cart = Cart.objects.create(is_active=True)
            cart.save()
            request.session['cart_id'] = cart.pk
    else:
        cart = Cart.objects.create(is_active=True)
        cart.save()
        request.session['cart_id'] = cart.pk
    return render(request, 'about_tea.html', {'cart': cart, 'about_tea': AboutTeaContent.objects.first()})


def payment_submission(request):
    if cart_pk := request.session.get('cart_id', False):
        try:
            cart = Cart.objects.get(pk=cart_pk)
        except ObjectDoesNotExist:
            cart = None
        if cart is None:
            cart = Cart.objects.create(is_active=True)
            cart.save()
            request.session['cart_id'] = cart.pk
    else:
        cart = Cart.objects.create(is_active=True)
        cart.save()
        request.session['cart_id'] = cart.pk
    return render(request, 'payment_submission.html', {'cart': cart, 'bank_props': BankProps.objects.first()})


def add_product_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if cart_pk := request.session.get('cart_id', False):
        try:
            cart = Cart.objects.get(pk=cart_pk)
        except ObjectDoesNotExist:
            cart = None
        if cart is None:
            cart = Cart.objects.create(is_active=True)
            cart.save()
            request.session['cart_id'] = cart.pk
    else:
        cart = Cart.objects.create(is_active=True)
        cart.save()
        request.session['cart_id'] = cart.pk
    product_to_cart = ProductToCart.objects.get_or_create(product=product, cart=cart)

    product_to_cart[0].quantity += 1
    product_to_cart[0].save()
    return redirect(reverse('shop:cart'))


def remove_product_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if cart_pk := request.session.get('cart_id', False):
        try:
            cart = Cart.objects.get(pk=cart_pk)
        except ObjectDoesNotExist:
            cart = None
        if cart is None:
            cart = Cart.objects.create(is_active=True)
            cart.save()
            request.session['cart_id'] = cart.pk
    else:
        cart = Cart.objects.create(is_active=True)
        cart.save()
        request.session['cart_id'] = cart.pk
    product_to_cart = ProductToCart.objects.get(product=product, cart=cart)
    if product_to_cart.quantity > 0:
        product_to_cart.quantity -= 1
        product_to_cart.save()
    else:
        product_to_cart.delete()
    return redirect(reverse('shop:cart'))


def cart_detail(request):
    if cart_pk := request.session.get('cart_id', False):
        try:
            cart = Cart.objects.get(pk=cart_pk)
        except ObjectDoesNotExist:
            cart = None
        if cart is None:
            cart = Cart.objects.create(is_active=True)
            cart.save()
            request.session['cart_id'] = cart.pk
    else:
        cart = Cart.objects.create(is_active=True)
        cart.save()
        request.session['cart_id'] = cart.pk
    products = [{'id': product_to_cart.product.pk, 'name': product_to_cart.product.name, 'price': product_to_cart.product.price, 'quantity': product_to_cart.quantity, 'sum': product_to_cart.products_sum()} for product_to_cart in cart.products_to_cart.all()]

    cart_json = {'products': products, 'sum': cart.all_products_sum(), 'products_quantity': cart.all_products_quantity()}

    return JsonResponse(cart_json)


def product_to_cart_detail(request, product_to_cart_id):
    product_to_cart = get_object_or_404(ProductToCart, pk=product_to_cart_id)

    json = {
        'id': product_to_cart.pk,
        'name': product_to_cart.product.name,
        'price': product_to_cart.product.price,
        'quantity': product_to_cart.quantity,
        'sum': product_to_cart.products_sum()
    }

    return JsonResponse(json)


def order_information(request):
    if cart_pk := request.session.get('cart_id', False):
        try:
            cart = Cart.objects.get(pk=cart_pk)
        except ObjectDoesNotExist:
            cart = None
        if cart is None:
            cart = Cart.objects.create(is_active=True)
            cart.save()
            request.session['cart_id'] = cart.pk
    else:
        cart = Cart.objects.create(is_active=True)
        cart.save()
        request.session['cart_id'] = cart.pk
    return render(request, 'order_information.html', {'cart': cart})


class OrderShippingView(CreateView):
    model = Order
    template_name = 'order_information.html'
    form_class = OrderShippingForm

    def get_context_data(self, *args, **kwargs):
        if cart_pk := self.request.session.get('cart_id', False):
            try:
                cart = Cart.objects.get(pk=cart_pk)
            except ObjectDoesNotExist:
                cart = None
            if cart is None:
                cart = Cart.objects.create(is_active=True)
                cart.save()
                request.session['cart_id'] = cart.pk
        else:
            cart = Cart.objects.create(is_active=True)
            cart.save()
            request.session['cart_id'] = cart.pk
        context = super().get_context_data()
        context['cart'] = cart
        return context

    def get_initial(self):
        initial = super().get_initial()
        if order_pk := self.request.session.get('order_id', False):
            order = get_object_or_404(Order, pk=order_pk)
            initial['email'] = order.email
            initial['shipping_first_name'] = order.shipping_first_name
            initial['shipping_last_name'] = order.shipping_last_name
            initial['shipping_address'] = order.shipping_address
            initial['shipping_city'] = order.shipping_city
            initial['shipping_province'] = order.shipping_province
            initial['shipping_postal'] = order.shipping_postal
            initial['shipping_phone'] = order.shipping_phone
        return initial

    def form_valid(self, form):
        cart = Cart.objects.get(pk=self.request.session.get('cart_id', False))
        order_pk = self.request.session.get('order_id', False)
        if not order_pk:
            self.object = form.save()
            self.object.save()
            self.request.session['order_id'] = self.object.pk
        else:
            order = get_object_or_404(Order, pk=order_pk)
            order.email = form.cleaned_data['email']
            order.shipping_first_name = form.cleaned_data['shipping_first_name']
            order.shipping_last_name = form.cleaned_data['shipping_last_name']
            order.shipping_address = form.cleaned_data['shipping_address']
            order.shipping_city = form.cleaned_data['shipping_city']
            order.shipping_province = form.cleaned_data['shipping_province']
            order.shipping_postal = form.cleaned_data['shipping_postal']
            order.shipping_phone = form.cleaned_data['shipping_phone']
            order.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        anchor = next((form[k].name for k in form.fields.keys() if form[k].errors), None)

        return self.render_to_response(self.get_context_data(form=form, anchor=anchor))

    def get_success_url(self):
        return reverse('shop:order_payment')


class OrderPaymentView(FormView):
    model = Order
    template_name = 'order_payment.html'
    form_class = OrderPaymentForm

    def get_context_data(self, *args, **kwargs):
        if cart_pk := self.request.session.get('cart_id', False):
            try:
                cart = Cart.objects.get(pk=cart_pk)
            except ObjectDoesNotExist:
                cart = None
            if cart is None:
                cart = Cart.objects.create(is_active=True)
                cart.save()
                request.session['cart_id'] = cart.pk
        else:
            cart = Cart.objects.create(is_active=True)
            cart.save()
            request.session['cart_id'] = cart.pk
        order_pk = self.request.session.get('order_id', False)
        if not order_pk:
            return redirect(reverse('shop:main'))
        context = super().get_context_data()
        order = get_object_or_404(Order, pk=order_pk)
        if order.is_active:
            context['cart'] = cart
            context['bank_props'] = BankProps.objects.first()
            context['order'] = order
            return context
        return redirect(reverse('shop:order_information'))

    def get_initial(self):
        initial = super().get_initial()
        if order_pk := self.request.session.get('order_id', False):
            order = get_object_or_404(Order, pk=order_pk)
            initial['billing_first_name'] = order.shipping_first_name
            initial['billing_last_name'] = order.shipping_last_name
            initial['billing_address'] = order.shipping_address
            initial['billing_city'] = order.shipping_city
            initial['billing_province'] = order.shipping_province
            initial['billing_postal'] = order.shipping_postal
            initial['billing_phone'] = order.shipping_phone
        return initial

    def form_valid(self, form):
        cart = Cart.objects.get(pk=self.request.session['cart_id'])
        order = get_object_or_404(Order, pk=self.request.session['order_id'])
        order.cart = cart
        order.billing_first_name = form.cleaned_data['billing_first_name']
        order.billing_last_name = form.cleaned_data['billing_last_name']
        order.billing_address = form.cleaned_data['billing_address']
        order.billing_city = form.cleaned_data['billing_city']
        order.billing_province = form.cleaned_data['billing_province']
        order.billing_postal = form.cleaned_data['billing_postal']
        order.billing_phone = form.cleaned_data['billing_phone']
        order.is_active = False
        order.save()
        cart.is_active = False
        cart.save()
        return super().form_valid(form)

    def get_success_url(self):
        order = get_object_or_404(Order, pk=self.request.session['order_id'])
        return reverse('shop:order_confirmation', kwargs={'order_id': order.pk})


def order_confirmation(request, order_id):
    if request.session.get('cart_id', False):
        del request.session['cart_id']
    if request.session.get('order_id', False):
        if str(request.session.get('order_id', False)) == str(order_id):
            order = get_object_or_404(Order, pk=request.session['order_id'])
            msg = render_to_string('email/order_email.html', {'order_url': f'http://localhost:8000/admin/shop/order/{order.pk}/change/', 'cart_url': f'https://leafshop.online/admin/shop/cart/{order.cart.pk}/change/', 'order_number': order.pk})

            email_thread(msg)
            request.session['finished_orders'] = request.session['finished_orders'].append(request.session['order_id']) if request.session.get('finished_orders', False) else [request.session['order_id']]

            del request.session['order_id']
        elif request.session.get('finished_orders', False):
            if order_id in request.session.get('finished_orders', False):
                pass
        else:
            return redirect(reverse('shop:main'))
    elif request.session.get('finished_orders', False):
        if int(order_id) not in request.session.get('finished_orders', False):
            return redirect(reverse('shop:main'))
    else:
        return redirect(reverse('shop:main'))
    if cart_pk := request.session.get('cart_id', False):
        try:
            cart = Cart.objects.get(pk=cart_pk)
        except ObjectDoesNotExist:
            cart = None
        if cart is None:
            cart = Cart.objects.create(is_active=True)
            cart.save()
            request.session['cart_id'] = cart.pk
    else:
        cart = Cart.objects.create(is_active=True)
        cart.save()
        request.session['cart_id'] = cart.pk
    order = Order.objects.get(pk=order_id)
    order_cart = Cart.objects.get(order=order)
    return render(request, 'order_confirmation.html', {'order_cart': order_cart, 'cart': cart, 'order': order, 'bank_props': BankProps.objects.first()})


def google(request):
    return render(request, 'search/googlebd43c182fd3d8564.html')
