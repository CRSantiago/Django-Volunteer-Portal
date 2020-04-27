from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact')
    
    GATEWAY_HIGH = 'GWHS'
    STCLOUD_HIGH = 'SCHS'
    CELEBRATION_HIGH = 'CHS'
    OSCEOLA_HIGH = 'OHS'
    PATHS = 'PATHS'
    HARMONY_HIGH = 'HHS'
    POINCIANA_HIGH = 'PHS'
    NEO_CTY = 'NCHS'
    LIBERY_HIGH = 'LHS'
    NEW_DIMENSIONS_HIGH = 'NDHS'
    NEW_BEGINNINGS = 'NEW-BEG'

    SCHOOL_CHOICES = [
        (GATEWAY_HIGH, 'Gateway High School'),
        (STCLOUD_HIGH, 'St. Cloud High School'),
        (CELEBRATION_HIGH, 'Celebration High School'),
        (OSCEOLA_HIGH, 'Osceola High School'),
        (PATHS, 'PATHS'),
        (HARMONY_HIGH, 'Harmony High School'),
        (POINCIANA_HIGH, 'Poinciana High School'),
        (NEO_CTY, 'Neocity Academy'),
        (LIBERY_HIGH, 'Libery High School'),
        (NEW_DIMENSIONS_HIGH, 'New Dimensions High School'),
        (NEW_BEGINNINGS, 'New Beginnings'),
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    D_O_B = models.DateField()
    parent_first_name = models.CharField(max_length=20)
    parent_last_name = models.CharField(max_length=20)
    parent_cell_phone = PhoneNumberField(region='US')
    school = models.CharField(max_length=30, choices=SCHOOL_CHOICES)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=7,default='Florida')
    zipcode = models.CharField(max_length=5)
    is_complete = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('contacts:contact-detail', kwargs={'id':self.id})
