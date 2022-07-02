from django.db import models

# Create your models here.
class SherlockUser(models.Model):
    username = models.CharField(max_length=150)
    link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username