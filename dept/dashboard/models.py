from django.db import models

# Create your models here.
class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    dept_code = models.CharField(max_length=10)
    dept_head = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.dept_id} ({self.dept_code})"