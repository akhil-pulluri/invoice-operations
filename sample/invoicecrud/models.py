from django.db import models
import uuid

def invoiceHeader(models.Model):
    id = models.UUIDField(primary_key=true)
    date = models.CharField(max_length=100)
    invoiceNumber = models.IntegerField()
    customerName = models.CharField(max_length=100)
    billingAddress = models.CharField(max_length=500)
    shippingAddress = models.CharField(max_length=500)
    gstIn = models.CharField(max_length=100)
    totalAmount = models.DecimalField()

def invoiceItem(models.Model):
    invoiceId = models.ForeignKey(invoiceHeader, on_delete = models.CASCADE)
    id = models.UUIDField(primary_key=true)
    itemName = models.CharField(max_length=100)
    quantity = models.DecimalField()
    price = models.DecimalField()
    amount = models.DecimalField()

def invoiceBillSundry(models.Model):
    invoiceId = models.ForeignKey(invoiceHeader, on_delete = models.CASCADE)
    id = models.UUIDField(primary_key=true)
    billSundryName = models.CharField(max_length=100)
    amount = models.DecimalField()