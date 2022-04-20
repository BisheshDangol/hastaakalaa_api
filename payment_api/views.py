from urllib import request
from crum import get_current_user
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework import generics
from art.models import Art
from art_api.serializers import ArtSerializer
from follow import models
from follow.models import Follow
from payment.models import Payment
from users.models import NewUser
from .serializers import PaymentSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from rest_framework.generics import GenericAPIView


class CreatePayment(APIView):
    def post(self, request, art):
        user_id = self.request.user.id
        
            
        data = { 'art_id': art, 'buyer_id': user_id, 'seller_id': request.data['seller_id'], 'price': request.data['price']}
        
        print('===========')
        print(request.data)
        print('===========')

        serializer = PaymentSerializer(data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        a = Art.objects.get(id=art)
        a.for_sale = False
        a.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetPaymentUser(generics.ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Payment.objects.filter(buyer_id=user)
