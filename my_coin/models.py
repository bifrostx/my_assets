from django.db import models


class Token(models.Model):
    name = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    price = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, editable=False)
    balance = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, editable=False)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Token, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
