from django.db import models
from django.utils import timezone

class VideoList(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-pub_date',)
    def __str__(self):
        return self.name
