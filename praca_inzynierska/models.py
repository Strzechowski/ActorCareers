from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class Actor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100, blank=True, null=True)
    surname = models.CharField(max_length = 100, blank=True, null=True)
    email = models.EmailField()
    city = models.CharField(max_length = 100, blank=True, null=True)
    last_role = models.CharField(max_length = 100, blank=True, null=True)
    last_movie = models.CharField(max_length = 100, blank=True, null=True)
    visible = models.CharField(
        choices = [
            ('Yes', 'Yes'),
            ('No', 'No'),
        ],
        max_length = 5
    )
    age = models.IntegerField(
        validators = [MaxValueValidator(120), MinValueValidator(1)],
        blank=True,
        null=True
    )
    sex = models.CharField(
        choices = [
            ('Man', 'Man'),
            ('Woman', 'Woman'),
        ],
        max_length = 5,
        blank=True,
        null=True
    )
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now = True, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='photos/profile_picture/', default='photos/profile_picture/default_profile_picture.png', blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    logo = models.ImageField(upload_to='photos/logos/', default='photos/logos/default_logo.jpg', blank=True, null=True)
    description = models.TextField()


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    pay_monthly = models.IntegerField(
        validators = [MaxValueValidator(120000), MinValueValidator(0)]
    )
    localization = models.CharField(max_length = 100)
    picture = models.ImageField(upload_to='photos/job_pictures/', default='photos/logos/defaul_logo.jpg', blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)

