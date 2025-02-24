from django.contrib import admin
from .models import SubscriptionsModel, UserSubscriptionModel, UserPaymentOrderModel
# Register your models here.
admin.site.register(SubscriptionsModel)
admin.site.register(UserSubscriptionModel)
admin.site.register(UserPaymentOrderModel)