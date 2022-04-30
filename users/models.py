from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField




# Create your models here.
class MpesaPayment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False,)
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
    Profile_image=CloudinaryField('image', null=True, blank=True)
    address=models.IntegerField()
    Upload_Cv=models.CharField(max_length=255)
    

class Jobseeker(models.Model):
    EDUCATION_TYPE = [
        ('C', 'Certificate'),
        ('D', 'Degree'),
        ('M', 'Masters'),
    ]

    jobid =  models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    location= models.IntegerField(blank=True)
    professsion=models.CharField(max_length=255)
    jobtype=models.CharField(max_length=255)
    experience=models.CharField(max_length=255)
    Education_level=models.CharField(max_length=2, choices=EDUCATION_TYPE)
    job_category=models.CharField(max_length=255)
    Phone_no=models.CharField(max_length=255)
    salary_Expectation=models.IntegerField()
    status=models.IntegerField()
    # file=models.FileField(null=False, blank=False)
    profile_pic=CloudinaryField('image', null=True, blank=True)
    bio=models.CharField(max_length=255)
    work=models.CharField(max_length=255)
    Education=models.CharField(max_length=255)
    skills=models.CharField(max_length=255)
    reference=models.CharField(max_length=255)



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


class Employer(models.Model):
    id =  models.IntegerField(Post, primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    contact=models.IntegerField()
    location= models.IntegerField(blank=True)
    address=models.CharField(max_length=255)
    company_bio=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    company_pic=CloudinaryField('image', null=True, blank=True)


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)
    is_jobseeker = models.ForeignKey(Jobseeker, on_delete=models.CASCADE, related_name='user')
    is_employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='user')

    REQUIRED = []

    def __str__(self):
        return f'{self.username}User'

    def save_user(self):
        super().save()

    @classmethod
    def get_user(cls):
        user=User.objects.all()
        return user

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
    
   