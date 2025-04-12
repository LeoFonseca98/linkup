from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_post')
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    
    def __str__(self):
        return self.title