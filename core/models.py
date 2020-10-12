from django.db import models
from . import managers


class TimeStampedModel(models.Model):

    """ Time Stamped Model"""

    created = models.DateTimeField(
        auto_now_add=True
    )  # Model이 생성된 날짜를 구하려면 auto_now_add사용
    updated = models.DateTimeField(auto_now=True)  # 새로운 날짜로 업데이트 auto_now
    objects = managers.CustomModelManager()

    class Meta:
        abstract = True  # don't enter database
