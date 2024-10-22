from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    is_vulnerable = models.BooleanField(default=False)

class EmailInteraction(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    clicked_link = models.BooleanField(default=False)
    response_time = models.DateTimeField(auto_now_add=True)
