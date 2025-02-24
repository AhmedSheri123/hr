from django.db import models
from django.utils.translation import gettext_lazy as _

class ParentOrganization(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField(blank=True, null=True)
    subscription = models.OneToOneField("subscriptions.UserSubscriptionModel", verbose_name=_("Subscription"), on_delete=models.SET_NULL, null=True, blank=True)
    
    setup_end = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    



