from django.db import models
from django.utils.text import slugify

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    profile_pic = models.ImageField(upload_to='profile/')
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=300, blank=True)
    bio = models.TextField(blank=True)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username
        


