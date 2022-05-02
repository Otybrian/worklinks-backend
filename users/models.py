from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField




# Create your models here.
class MpesaPayment(models.Model):
    amount = models.DecimalField(max_digits=10, blank=False, decimal_places=2)
    description = models.TextField()
    type = models.TextField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.TextField()

    class Meta:
        verbose_name = "Mpesa Payment"
        verbose_name_plural = "Mpesa Payments"

    def __str__(self):
        return self.first_name

class Profile(models.Model):
    id =  models.IntegerField(User, primary_key=True)
    Full_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    contact=models.CharField(max_length=255)
    Profile_image=CloudinaryField('image')
    address=models.IntegerField()
    Upload_Cv=models.CharField(max_length=255)
    
class User(AbstractUser):
    USERNAME_FIELD = 'username'
    is_admin = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    is_jobseeker = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def save_user(self):
        self.save()

    def update_user(self):
        self.update()

    def delete_user(self):
        self.delete()


class Employer(models.Model):
    user=  models.OneToOneField(User, blank=True, on_delete=models.CASCADE, primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    contact=models.IntegerField()
    location= models.IntegerField(blank=True)
    address=models.CharField(max_length=255)
    company_bio=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    company_pic=CloudinaryField('image' )

class Jobseeker(models.Model):
    user = models.OneToOneField(Employer, on_delete=models.CASCADE, primary_key=True)
    profile_photo = CloudinaryField('image',  blank=True)
    bio = models.TextField( blank=True)
    location = models.CharField(max_length=100,  blank=True)
    contact = models.CharField( max_length=30,  blank=True)
    availability = models.CharField( blank=True,  max_length=20)
    salary = models.IntegerField( )
    name = models.IntegerField( blank=False )
    phone_no= models.CharField(max_length=50 , blank=False)
    email = models.CharField(max_length=50 , blank=True )
    password= models.CharField(max_length=50, blank=False)
    

    def save_jobseeker(self):
        self.save()

    def delete_jobseeker(self):
        self.delete()

    @classmethod
    def update_jobseeker(self):
        self.update()

    @classmethod
    def search_jobseekers_by_job_category(cls, job_category):
        jobseekers = Jobseeker.objects.filter(
            job_category__icontains=job_category)
        return jobseekers




class Post(models.Model):
    id =  models.IntegerField( primary_key=True)
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    # file=models.FileField()

def __str__(self):
        return f'{self.title}'

def delete_post(self):
        self.delete()

@classmethod
def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

@classmethod
def all_posts(cls):
        return cls.objects.all()

def save_post(self):
        self.save()
class Comment(models.Model):
    id =  models.IntegerField(primary_key=True ) 
    userId=models.IntegerField()
    content=models.CharField(max_length=255)
    post=models.CharField(max_length=255)
    like=models.IntegerField()
    dislike=models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.user.name} post'


    def delete_user(self):
        self.delete()

class Job(models.Model):
     JOB_TYPE = [
        ('Part Time', 'Part-Time'),
        ('Remote', 'Remote'),
        ('Full Time', 'Full-Time'),
     ]
     title= models.CharField(max_length=30)
     location = models.CharField(max_length=255)
     requirements = models.TextField()
     jobtype= models.TextField(max_length=30, choices=JOB_TYPE)

     def save_job(self):
        self.save()

     def delete_job(self):
        self.delete()

     def __str__(self):
        return self.title
    
   