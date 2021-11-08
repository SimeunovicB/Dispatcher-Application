from django.db import models
from django.contrib.auth.models import AbstractUser
from enumchoicefield import ChoiceEnum, EnumChoiceField
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return "First name: {}, Email: {}".format(self.firstName, self.email)


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
    No_priority = "No_priority"
    Future = "Future"
    Hot = "Hot"
    Bad = "Bad"
    Booked = "Booked"


class Lead(models.Model):
    first_name = models.CharField(max_length=255, null=True)  #
    last_name = models.CharField(max_length=255, null=True)  #
    email = models.EmailField(max_length=254)  #
    phone = models.CharField(max_length=255, null=True)  #
    # time_created = models.DateTimeField(auto_now_add=True, null=True) #
    time_created = models.CharField(max_length=255, null=True)
    # last_changed = models.DateTimeField(auto_now_add=True, null=True) #
    last_changed = models.CharField(max_length=255, null=True)
    year1 = models.CharField(max_length=255, null=True)  #
    make1 = models.CharField(max_length=255, null=True)
    model1 = models.CharField(max_length=255, null=True)  #
    vehicle_type_id1 = models.CharField(max_length=255, null=True)  #
    vehicle_runs = models.CharField(max_length=255, null=True)  #
    ship_via_id = models.CharField(max_length=255, null=True)
    pickup_city = models.CharField(max_length=255, null=True)
    pickup_state_code = models.CharField(max_length=255, null=True)
    pickup_zip = models.CharField(max_length=255, null=True)  #
    dropoff_city = models.CharField(max_length=255, null=True)
    dropoff_state_code = models.CharField(max_length=255, null=True)
    dropoff_zip = models.CharField(max_length=255, null=True)
    estimated_ship_date = models.CharField(max_length=255, null=True)
    priority = EnumChoiceField(enum_class=PRIORITY, default=PRIORITY.No_priority)
    agent = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # TODO DA LI SE PRIKAZUJE LEAD JE ACTIVE
    active = models.BooleanField(default=False)
    notes_active = models.BooleanField(default=False)

    def __str__(self):
        return ("First name: {}, Last name: {}".format(self.first_name, self.last_name))

    # @receiver(post_save, sender=User)
    # def update_lead(sender, instance, created, **kwargs):
    #     if not created:
    #         print("Lead updated")
    #         print(instance)


def update_note(instance, *args, **kwargs):
    print("Note saved")


class Note(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    time = models.CharField(max_length=255, null=True)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, null=True)


@receiver(post_save, sender=Lead)
def create_lead(sender, instance, created, **kwargs):  # created proverava da li se sad trenutno pravimo

    if created:
        # Note.objects.create(lead=instance)
        print("Lead created!")


@receiver(post_save, sender=Lead)
def update_lead(sender, instance, created, *args, **kwargs):
    if not created:
        print("Lead updated!")


@receiver(post_save, sender=Note)
def create_note(sender, instance, created, *args, **kwargs):
    if created:
        print("Note created!")
