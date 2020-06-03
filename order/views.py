import os
from django.core.exceptions import PermissionDenied
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from decimal import Decimal

#For invoice PDF
from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice

from permission.services import APIPermissionClassFactory
from order.models import Order, OrderItem
from cart.models import Cart, CartItem

from order.serializers import OrderSerializer, OrderItemSerializer
from product.serializers import ProductSerializer

import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
from django.conf import settings

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='OrderPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, req: user.is_authenticated,
                    'list': lambda user, req: user.is_authenticated,
                    
                },
                'instance': {
                    'retrieve': lambda user, obj, req: user.is_authenticated,
                    'destroy': lambda user, obj, req: user.is_authenticated,
                    'update': lambda user, obj, req: user.is_authenticated,
                    'partial_update': lambda user, obj, req: user.is_authenticated,
                    'perform_create': lambda user, obj, req: user.is_authenticated,
                    'products': lambda user, obj, req: user.is_authenticated,
                    'process': lambda user, obj, req: user.is_authenticated,
                }
            }
        ),
    )

    def get_queryset(self):
        queryset = Order.objects.all()
        user_id = self.request.query_params.get('user', None)
        if user_id is not None:
            queryset = queryset.filter(user__id=user_id)
        return queryset

    # POST method
    def perform_create(self, serializer):
        user = self.request.user
        cart = Cart.objects.filter(user=user).first()
        order = serializer.save()
        assign_perm('order.change_order', user, order)
        assign_perm('order.view_order', user, order)
        
        if cart != None:
            cart_items = CartItem.objects.filter(cart=cart).all()
            self.create_order_items(order, cart_items, user)
            CartItem.objects.filter(cart=cart).delete()
            order.total = self.get_cart_total_amount(cart_items)
            order.save()

            # Generating PDF
            if user.email != None or user.email != '':
                self.generate_pdf(order, user)
                self.send_invoice_via_email(user.email)


        return Response(serializer.data)

    def generate_pdf(self, order, user):
        invoice_doc = SimpleInvoice('invoice.pdf')

        # Paid stamp, optional
        invoice_doc.is_paid = False
        invoice_doc.invoice_info = InvoiceInfo(order.id, datetime.now(), datetime.now())  # Invoice info, optional

        # Service Provider Info, optional
        invoice_doc.service_provider_info = ServiceProviderInfo(
            name='Azen Store',
            street='Somewhere in Guatemala',
            city='Guatemala',
            state='Guatemala',
            country='Guatemala',
            post_code='0100X',
        )

        order_items = OrderItem.objects.filter(order=order).all()

        # Client info, optional
        invoice_doc.client_info = ClientInfo(client_id= user.id, name=user.username)

        for order_item in order_items:
            # Add Item
            invoice_doc.add_item(Item(order_item.product.name, 'Item', order_item.quantity, order_item.product.price))
        
        # Tax rate, optional
        invoice_doc.set_item_tax_rate(0)  # 0%
        # Optional
        invoice_doc.set_bottom_tip("Email: info@azenstore.com<br />Don't hesitate to contact us for any questions.<br />Coupons are applied in payments...")

        invoice_doc.finish()

    def send_invoice_via_email(self, email):
        print("Sending email to {0}...".format(email))
        
        message = Mail(
            from_email='gus.mendez.99@gmail.com',
            to_emails=email,
            subject='New Order - Azen Store',
            html_content='<strong>Your order has been received. Thanks for your purchase.</strong>')


        with open(os.path.join(settings.BASE_DIR, "invoice.pdf"), 'rb') as f:
            file_data = f.read()
            f.close()
            
            encoded_file = base64.b64encode(file_data).decode()

            attachedFile = Attachment(
                FileContent(encoded_file),
                FileName('attachment.pdf'),
                FileType('application/pdf'),
                Disposition('attachment')
            )
            message.attachment = attachedFile

        sg = SendGridAPIClient("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")
        response = sg.send(message)
        print(response.status_code, response.body, response.headers)

    def get_cart_total_amount(self, cart_items ):
        total = 0.00
        for cart_item in cart_items:
            total += (cart_item.quantity) * float(cart_item.product.price)
        print("This is my order total: ", total)
        return Decimal.from_float(total)

    # GET method
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        order = self.get_object()
        queryset = order.products.all()
        data = ProductSerializer(queryset, many = True).data
        return Response(data)

    @action(detail=True, methods=['post'])
    def process(self, request, pk=None):
        order = self.get_object()
        self.change_status(order, 1)
        return Response(OrderSerializer(order).data)

    def create_order_items(self, order, cart_items, user):
        for cart_item in cart_items:
            order_item = OrderItem(
                order = order,
                product = cart_item.product,
                quantity = cart_item.quantity
            )
            order_item.save()
            assign_perm('orderitem.change_orderitem', user, order_item)
            assign_perm('orderitem.view_orderitem', user, order_item)

    def change_status(self, order, status):
        order.status = status
        order.save()
        print ("Order {} processed!".format(order))
            
