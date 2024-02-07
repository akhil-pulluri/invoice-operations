from rest_framework import serializers
from .models import invoiceHeader, invoiceItem, invoiceBillSundry

class invoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = invoiceItem
        fields = '__all__'

    def validate(self, data):

        if data['price'] <=0 or data['amount'] <= 0 or data['quantity'] <=0:
            raise serializers.ValidationError("Price, Quantity, and Amount must be greater than zero")

        if data['price'] * data['quantity'] != data['Amount']:
            raise serializers.ValidationError("Amount should be equal to product of price and quantity")

        return data

class billSundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = invoiceBillSundry
        fields = '__all__'

    def validate(self, data):

        if data['amount'] < 0 or data['amount'] > 0 or data['amount'] == 0:
            return data
        else:
            raise serializers.ValidationError("The amount can only be negative or positive or zero")


# class invoiceHeaderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = invoiceHeader
#         fields = '__all__'
#
#     def validate(self, data):
#         invoiceItems =
#         invoiceBillSundrys =
#         total =
