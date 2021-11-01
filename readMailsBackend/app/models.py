from django.db import models
from django.contrib.auth.models import AbstractUser
from enumchoicefield import ChoiceEnum, EnumChoiceField


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


# Create your models here.
# TODO NAPRAVI MODEL ZA PORUKU
class Message(models.Model):
    subject = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    sender = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    body = models.TextField()
    html_body = models.TextField()
    read = models.BooleanField(default=False)


class PRIORITY(ChoiceEnum):
    NO_PRIORITY = "No priority"
    FUTURE_LEAD = "Future lead"
    HOT_LEAD = "Hot lead"
    BAD_LEAD = "Bad lead"
    BOOKED_LEAD = "Booked lead"


class Lead(models.Model):
    name = models.CharField(max_length=255) #
    surname = models.CharField(max_length=255) #
    email = models.EmailField(max_length=254, unique=True) #
    phone_number = models.CharField(max_length=255) #
    time_created = models.DateTimeField() #
    last_changed = models.DateTimeField() #
    car_year = models.CharField(max_length=255) #
    car_model = models.CharField(max_length=255) #
    #make
    car_type = models.CharField(max_length=255) #
    car_condition = models.CharField(max_length=255) #
    carrier_type = models.CharField(max_length=255)
    pickup_city = models.CharField(max_length=255) #
    pickup_zip = models.CharField(max_length=255) #
    delivery_city = models.CharField(max_length=255)
    delivery_zip = models.CharField(max_length=255)
    move_date = models.DateTimeField()
    priority = EnumChoiceField(enum_class=PRIORITY, default=PRIORITY.NO_PRIORITY)
    agent = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

# class Note(models.Model):
#     sender =
#     message = models.TextField()
#     time = models.DateTimeField()
#     lead = models.ForeignKey(Lead)
