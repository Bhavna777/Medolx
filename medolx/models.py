from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField



departments=[
('Endocrine Disorders','Endocrine Disorders'),
('Dermatologists','Dermatologists'),
('Gyneology and Obstetrics','Gyneology and Obstetrics'),
('Pain Management','Pain Management'),
('Dietitian & Nutritionist','Dietitian & Nutritionist'),
('General Physician','General Physician'),
('Sexual Discorders','Sexual Discorders'),
('Lifestyle Disorders','Lifestyle Disorders'),
('Ear Nose Throat Specialist','Ear Nose Throat Specialist'),
('PANCHKARMA SPECIALIST','PANCHKARMA SPECIALIST'),
('SKIN & COSMETOLOGIST','SKIN & COSMETOLOGIST'),
('HAIR CARE & TRICHOLOGY','HAIR CARE & TRICHOLOGY'),
('PSYCOLOGIST','PSYCOLOGIST'),
('PAEDIATRIC','PAEDIATRIC'),
('DIABITIS SPACIAlist','DIABITIS SPACIAlist'),
('Covid Care','Covid Care'),

]


class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=35)
    phone_no = models.CharField(max_length=10)
    address = models.CharField(max_length=40)
    qualification = CharField(max_length=25)
    hospital_name = models.CharField(max_length=50)
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=gender)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    experience = CharField(max_length=5)
    consultation_fee = CharField(max_length=5)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)




class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, default=None)
    email=models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10)
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=gender)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.user.last_name)







class Product(models.Model):
    name = models.CharField(max_length=40)
    profile_pic= models.ImageField(upload_to='profile_pic/ProductProfilePic/',null=True,blank=True)
    used_for = models.CharField(max_length=40)
    rate = models.CharField(max_length=7,null=True)




class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    desc = models.CharField(max_length=300)
    featured_pic= models.ImageField(upload_to='blog_pic/BlogFeaturedPic/',null=True,blank=True)
    content = models.TextField()
    author = models.CharField(max_length=20)
    author_pic= models.ImageField(upload_to='blog_pic/BlogAuthorPic/',null=True,blank=True)
    
    def __str__(self):
        return self.title



class Contact(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=35)
    message = models.TextField()

    def __str__(self):
        return self.email


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)