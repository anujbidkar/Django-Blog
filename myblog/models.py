from django.db import models
from django.urls import reverse
# Create your models here.
class Myblog(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.FileField(upload_to='post_image',blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')