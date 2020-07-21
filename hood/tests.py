from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from .models import Profile,Neighbourhood
from django.test import TestCase
from .models import Image
class Intagram_TestCases(TestCase):
    def setUp(self):
        self.user1= User(id=1,username='Edgar',email='kipyego@gmail.com',password='admin.py')
        self.user1.save()
        self.neiba = Neighbourhood(id=1,name='sar',health_dpt_address='999', health_dpt='KMM')
        self.neiba.create_neigborhood()

        self.profile = Profile(bio='plucker',profile_path='image/image.jpg')
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.user1,User))
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.neiba,Neighbourhood))

    def test_save_method(self):
        self.neiba.create_neigborhood()
        all_objects = Neighbourhood.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        self.neiba.create_neigborhood()
        filtered_object = Neighbourhood.objects.filter(name='plucker')
        Image.delete_image(filtered_object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)

    def test_display_all_objects_method(self):
        self.neiba.create_neigborhood()
        all_objects = Neighbourhood.retrieve_all()
        self.assertEqual(all_objects.name,'plucker')


    def test_update_single_object_property(self):
        self.neiba.create_neigborhood()
        filtered_object =Neighbourhood.update_occupants('plucker','Yego')
        fetched = Profile.objects.get(community__name='Yego')
        self.assertEqual(fetched.name,'Yego')
    def test_find_neigborhood(self):
        self.neiba.create_neigborhood()
        fetched_image = Image.find_neigborhood(1)
        self.assertEqual(fetched_image.id,1)