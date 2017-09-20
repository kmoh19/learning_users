from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    
    user=models.OneToOneField(User) #basically extending the User class without 'inheriting' done to avoid confusion
    
    # additional 
    
    portfolio_site=models.URLField(blank=True)
    
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    
    
    def __str__(self):
        return self.user.username #username is an attribute of User class