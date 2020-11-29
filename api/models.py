from django.db import models

# Create your models here.

class CompanyScrip(models.Model):

    company_name = models.TextField()
    scrip_codes = models.TextField()
