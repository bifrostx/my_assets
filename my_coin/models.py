from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=10, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=4, default=0.0)
    price = models.DecimalField(max_digits=10, decimal_places=1, default=0.0, editable=False)
    balance = models.DecimalField(max_digits=10, decimal_places=1, default=0.0, editable=False)

    def __str__(self):
        return self.name


