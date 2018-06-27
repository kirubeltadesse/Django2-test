from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    # ADDING INFORMATION TO THE USER THAT IS NOT INCLUDED IN THE MODEL
    # BASICALL OneToOneField means that
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    # additional
    # black=True means the user doesn't need to provide their picture
    # if they don't want too
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
