from django.db import models
from django.urls import reverse


class List(models.Model):

    def get_absolute_url(self):
        return reverse("view_list", args=[self.id])


class Item(models.Model):
    
    text = models.TextField(default="")
    list = models.ForeignKey(List, models.CASCADE, default=None)

    class Meta:
        unique_together = ('list', 'text')
