from django.db import models

# Create your models here.
class NewsType(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class NewsDetail(models.Model):
    types = models.ForeignKey(to=NewsType, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    images_1 = models.ImageField(null=True,upload_to='news/images/')
    def __str__(self):
        return self.title + ' - ' + self.types.name