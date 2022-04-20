from django.urls import path

from payment_api.views import CreatePayment, GetPaymentUser 

app_name = 'payment_api'

urlpatterns = [
    path('payment/<int:art>', CreatePayment.as_view(), name='createpayment'),
    path('get_payment/', GetPaymentUser.as_view(), name='userpaymentlist'),

]