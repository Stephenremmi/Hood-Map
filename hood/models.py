from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64, null=True)
    created_by =  models.CharField(max_length=64, null=True)
    police = models.CharField(max_length=20)
    health_dpt = models.CharField(max_length=20)
    health_dpt_address = models.CharField(max_length=20)
    police_dpt_address = models.CharField(max_length=20)


    def __str__(self):
        return f' {self.name} Community'


    def get_absolute_url(self):
        return reverse('profile')
    @classmethod
    def find_neigborhood(cls,search_term):
        search_result = cls.objects.filter(bsn_name__icontains=search_term)
        return search_result   
    @classmethod
    def create_neigborhood(cls):
        cls.save()
    @classmethod
    def delete_neigborhood(cls, id):
        delet = cls.objects.filter(id=id).delete()
                   
    @classmethod
    def update_occupants(cls,id):
        bsn = cls.objects.filter(id=id).update()
        return bsn 


class Profile(models.Model):
    
    profile_path = models.ImageField(upload_to = 'profile_pics/',default='profile_pics/default.jpg')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    community = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True, related_name='population')

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def image(self):
        if self.profile_path and hasattr(self.profile_path, 'url'):
            return self.profile_path.url

    @classmethod
    def search_by_username(cls,search_term):
        search_result = cls.objects.filter(user__username__icontains=search_term)
        return search_result

    def save_profile(self):
        self.save()


class Post(models.Model):
    description =  models.CharField(max_length=70)
    post_image = models.ImageField(upload_to='images/', null=True,blank=True)
    categories = models.CharField(max_length=70)
    time_created =  models.DateTimeField(auto_now=True, null =True)
    location=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    user_profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
    def get_absolute_url(self):
        return reverse('home')        


class Business(models.Model):
    bsn_name = models.CharField(max_length=64, unique= True)
    bsn_user = models.ForeignKey(User,on_delete=models.CASCADE)
    bsn_community = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True)
    bsn_email = models.EmailField(max_length=64, unique= True) 
    def get_absolute_url(self):
        return reverse('home')  

    @classmethod
    def search_by_bsn(cls,search_term):
        search_result = cls.objects.filter(bsn_name__icontains=search_term)
        return search_result   
    @classmethod
    def create_business(cls, **kwargs):
        loca = Neighbourhood.objects.get(id=request.user.profile.community.id)  
        new_business = Business(bsn_name=bizna,bsn_user=request.user,bsn_community=loca,bsn_email=email)
        new_business.save()
    @classmethod
    def delete_business(cls, id):
        delet = cls.objects.filter(id=id).delete()
                   
    @classmethod
    def update_business(cls,id):
        bsn = cls.objects.filter(id=id).update()
        return bsn 

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment 