
from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    # seller_id = serializers.StringRelatedField()
    # buyer_id = serializers.StringRelatedField()
    class Meta: 
        model = Payment
        fields = ('id','seller_id', 'buyer_id', 'price')