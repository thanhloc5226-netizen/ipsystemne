from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    icon = models.ImageField(upload_to='service/icons/', null=True, blank=True)

    def __str__(self):
        return self.name