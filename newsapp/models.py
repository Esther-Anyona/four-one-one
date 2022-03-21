from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# CloudinaryImage("turtles.jpg").image(width=70, height=53, crop="scale")
"""
Models 
"""
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    description = models.TextField()
    occupants_count = models.IntegerField(null=True, blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood_pic = CloudinaryField('hood-pic')
    ambulance_contact = models.CharField(max_length=20, null=True, blank=True)
    police_contact = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_id = models.CharField(max_length=10, blank=True)
    profile_pic = CloudinaryField('profile-pic')
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)


class Business(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    biz_email = models.CharField(max_length=100)

    """
    methods
    """
    # create_business()
    # delete_business()
    # find_business(business_id)
    # update_business()



