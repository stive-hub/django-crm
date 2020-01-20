# import arrow
from django.db import models
# from django.phonenumber_field.modelfields import PhoneNumberField



class Contact(models.Model):
    first_name = models.CharField(("First name"), max_length=255)
    last_name = models.CharField(("Last name"), max_length=255)
    email = models.EmailField(unique=True)
    # phone = models.PhoneNumberField(null=True, unique=True)
    # description = models.TextField(blank=True, null=True)
    # assigned_to = models.ManyToManyField(
    #     User, related_name='contact_assigned_users')
    # created_by = models.ForeignKey(
    #     User, related_name='contact_created_by',
    #     on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(("Created on"), auto_now_add=True)
    # is_active = models.BooleanField(default=False)
    # teams = models.ManyToManyField(Teams, related_name='contact_teams')
    address_line = models.CharField(
        ("Address"), max_length=255, blank=True, null=True)
    street = models.CharField(
        ("Street"), max_length=55, blank=True, null=True)
    city = models.CharField(("City"), max_length=255, blank=True, null=True)
    state = models.CharField(("State"), max_length=255, blank=True, null=True)
    postcode = models.CharField(
        ("Post/Zip-code"), max_length=64, blank=True, null=True)
    # country = models.CharField(
    #     max_length=3, choices=COUNTRIES, blank=True, null=True)


    def __str__(self):
        return self.first_name

    # @property
    # def created_on_arrow(self):
    #     return arrow.get(self.created_on).humanize()

    # class Meta:
    #     ordering = ['-created_on']

