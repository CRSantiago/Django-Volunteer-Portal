from django.db import models

from django.contrib.auth.models import User

class Log(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')

   date = models.DateField()
   hours_completed = models.DecimalField(max_digits=4, decimal_places=2)
