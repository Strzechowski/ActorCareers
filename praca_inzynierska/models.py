from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Announcement(models.Model):
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    age = models.IntegerField(
        validators = [MaxValueValidator(120), MinValueValidator(1)]
    )
    sex = models.CharField(
        choices = [
            ('Man', 'Man'),
            ('Woman', 'Woman'),
        ],
        max_length = 5,
    )
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    profile_picture = models.ImageField(upload_to='photos/profile_picture/', default='photos/profile_picture/default_profile_picture.png', blank=True, null=True)

class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super().delete(*args,**kwargs)

