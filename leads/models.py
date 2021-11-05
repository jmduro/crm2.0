from django.db import models
from django.db.models.signals import post_save
from users.models import User

# class UserProfile(models.Model):
#     user = models.OneToOneField('User', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username

# class User(AbstractUser):
#     first_name = models.CharField(max_length = 20, unique=True)
#     last_name = models.CharField(max_length = 20)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=20, unique=True)
#     is_organisor = models.BooleanField(default=True)
#     is_agent = models.BooleanField(default=False)

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length = 50)
    email = models.EmailField()
    agent = models.ForeignKey('Agent', null = True, blank = True, on_delete = models.SET_NULL)
    mobile = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    home_phone = models.CharField(max_length =20)
    description = models.TextField()

    organisation = models.ForeignKey(User, on_delete = models.CASCADE)
    
    category = models.ForeignKey('Category', related_name='leads', null = True, blank = True, on_delete=models.SET_NULL)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Agent(models.Model):
    company_name = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length = 20, unique=True)
    website = models.CharField(max_length = 100, unique=True)
    description = models.TextField()
    billing_street = models.CharField(max_length=50)
    billing_city = models.CharField(max_length=50)
    billing_State = models.CharField(max_length =50)
    billing_country = models.CharField(max_length =50)
    billing_code =models.CharField(max_length=50)

    organisation = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name

# class Product(models.Model):
#     product_name = models.CharField(max_length=20, unique=True)
#     product_code = models.CharField(max_length =20, unique=True)
#     category = models.CharField(max_length =30)
#     unit_price = models.FloatField()
#     description = models.TextField()
#     organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.product_name

# class Deal(models.Model):
#     deal_name = models.CharField(max_length=20, unique=True)
#     contact_name = models.ForeignKey('Lead', null = True, blank = True, on_delete = models.SET_NULL)
#     company_name = models.ForeignKey('Agent', null = True, blank = True, on_delete = models.SET_NULL)
#     stage = models.ForeignKey('Stage', related_name ='deals', null = True, blank = True, on_delete = models.SET_NULL)
#     amount = models.FloatField()
#     closing_date = models.DateField()
#     description = models.TextField()
#     product = models.ForeignKey('Product', null = True, blank = True, on_delete = models.SET_NULL)
#     organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.deal_name

# class Task(models.Model):
#     task_name = models.CharField(max_length=50, unique=True)
#     due_date = models.DateField()
#     repeat = models.CharField(max_length=50, unique=True)
#     related_to = models.CharField(max_length =50, unique=True)
#     description = models.TextField()
#     priority = models.CharField(max_length=50)

#     organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.task_name

# class Event(models.Model):
#     title = models.CharField(max_length=50, unique=True)
#     From = models.CharField(max_length =50)
#     to = models.CharField(max_length =50)
#     repeat = models.CharField(max_length=50)
#     location = models.CharField(max_length=50)
#     related_to = models.CharField(max_length=50)
#     description = models.TextField()
    
#     organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

# class Stage(models.Model):
#     name = models.CharField(max_length=30, unique=True)
#     organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Category(models.Model):
#     name = models.CharField(max_length=30, unique=True)
#     organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# def post_user_created_signal(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# post_save.connect(post_user_created_signal, sender = User)