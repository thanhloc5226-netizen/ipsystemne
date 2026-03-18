from django.db import models

# Create your models here.
class Portfolio(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    challenges = models.TextField(null=True, help_text='Thách thức và giải pháp')
    achievements = models.TextField(null=True, help_text='Kết quả đạt được')
    url = models.URLField(null=True, help_text='Đường dẫn tới trang web của dự án')
    image = models.ImageField(upload_to='portfolio/images/')
    def __str__(self):
        return self.title

class Portfolio_Image(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/images/')
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.portfolio.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
