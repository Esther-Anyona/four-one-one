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

    def create_neigbourhood(self):
        self.save()

    def get_neighbourhoods(self):
        neighbourhoods = Neighbourhood.objects.all()
        return neighbourhoods


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_id = models.CharField(max_length=10, blank=True)
    profile_pic = CloudinaryField('profile-pic')
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        super().save()

class Business(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='Business_owner')
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='Hood')
    business_email = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f'{self.name}Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business = cls.objects.get(id = business_id)
        return business

    def update_business(self, id, name, description, user, neighbourhood_id, biz_email):
        update = NeighbourHood.objects.filter(id = id).update(name = name , description = description, user=user, neighbourhood_id = neighbourhood_id, biz_email = biz_email)
        return update
    """
    methods
    """
    # create_business()
    # delete_business()
    # find_business(business_id)
    # update_business()

class Post(models.Model):
    title = models.CharField(max_length=50, null=True)
    post = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='Author')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='Hood_post')

    def __str__(self):
        return f'{self.title} Post'    
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()


