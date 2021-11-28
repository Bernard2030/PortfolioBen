from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
# Model for Home Page
class Home(models.Model):
    name = models.CharField(max_length=200)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=5)
    image = CloudinaryField('image')

    # show time when uploaded
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


#  Model for About Page

class About(models.Model):
    heading = models.CharField(max_length=50)
    carreer = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profileimage = CloudinaryField('image')

    # show time when uploaded
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.carreer


#profile

class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=20)
    social_link = models.URLField(max_length=200)


#  Skills section

class Category(models.Model):
    name = models.CharField(max_length=20)
    uploaded = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'


    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skills_name = models.CharField(max_length=20)
    


    def __str__(self):
        return self.name 


# Portfolio section

class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    portfolio_image = CloudinaryField('image')
    link = models.URLField(max_length=200)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



    
