from django.db import models

# Create your models here.

class XLSX(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
