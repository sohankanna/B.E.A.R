from django.db import models

class Organization(models.Model):
    org_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)  # You can later hash this if needed

    def __str__(self):
        return self.org_name
