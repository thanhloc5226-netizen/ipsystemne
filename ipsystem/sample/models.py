from django.db import models

# Create your models here.
class Sample(models.Model):
    class Type(models.TextChoices):
        DOANH_NGHIEP = 'doanh-nghiep', 'Doanh nghiệp'
        THUONG_MAI = 'thuong-mai', 'Thương mại điện tử'
        QUAN_LY = 'quan-ly', 'Quản lý nội bộ'
        KHAC = 'khac', 'Khác'

    type = models.CharField(max_length=20, choices=Type.choices)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_1 = models.ImageField(upload_to='samples/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='samples/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='samples/', null=True, blank=True)

    def __str__(self):
        return self.title