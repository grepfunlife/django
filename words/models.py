from django.conf import settings
from django.db import models

class List(models.Model):
    title = models.CharField(max_length=200)
    count = models.BigIntegerField
    answer = models.ExpressionList
    done = models.BooleanField(default=False)

    def addList(self):
        self.save()

    def _str_(self):
        return self.title


