from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
user = User.objects.get(id=1)
profile = Profile.objects.get(id=1)
neighbourhood = Neighbourhood.objects.get(id=1)


class TestBusiness(TestCase):
    def setUp(self):
        self.business=Business(name = "hardware", description="your stop for best prices", user= profile, neighbourhood_id=neighbourhood, business_email='mail@gmail.com')
        self.business.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def test_create_business(self):
        self.business.create_business()
        businesses=Business.objects.all()
        self.assertTrue(len(businesses)>0)

    def test_delete_business(self):
        self.business.delete_business()
        businesses=Business.objects.all()
        self.assertTrue(len(businesses)==0)

    def test_update_business(self):
        self.business.create_business()
        # self.business.update_business(self.business.id, 'hardware')
        updated_business = Business.objects.all()
        self.assertTrue(len(updated_business) > 0)

    def tearDown(self):
        Business.objects.all().delete()

 

    
