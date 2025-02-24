"""
horilla_company_manager.py
"""

import logging
from typing import Coroutine, Sequence

from django.db import models
from django.db.models import Q

from django.db.models.query import QuerySet

from horilla.horilla_middlewares import _thread_locals
from horilla.signals import post_bulk_update, pre_bulk_update
logger = logging.getLogger(__name__)
django_filter_update = QuerySet.update


def update(self, *args, **kwargs):
    # pre_update signal
    request = getattr(_thread_locals, "request", None)
    self.request = request
    pre_bulk_update.send(sender=self.model, queryset=self, args=args, kwargs=kwargs)
    result = django_filter_update(self, *args, **kwargs)
    # post_update signal
    post_bulk_update.send(sender=self.model, queryset=self, args=args, kwargs=kwargs)

    return result

setattr(QuerySet, "update", update)

class OrganizationManager(models.Manager):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def get_queryset(self):
        request = getattr(_thread_locals, "request", None)
        queryset = super().get_queryset()

        if not request or not hasattr(request, "user"):
            return queryset  # لا يوجد طلب، نعيد كل البيانات بدون تصفية

        user = request.user
        if not user.is_authenticated:
            return queryset  # المستخدم غير مسجل الدخول

        if hasattr(user, "employee_get") and user.employee_get.parent:
            parent_organization = user.employee_get.parent
            parent_field = getattr(self.model, "parent", None)
            modified_by_field = getattr(self.model, "modified_by", None)

            if parent_field:
                return queryset.filter(parent=parent_organization)
            elif modified_by_field:
                return queryset.filter(modified_by__employee_get__parent=parent_organization)

        return queryset.none()

    
    def all(self):
        return self.get_queryset()

    def filter(self, *args, **kwargs):
        return self.get_queryset().filter(*args, **kwargs)

    def get_all(self):
        return self.get_queryset()