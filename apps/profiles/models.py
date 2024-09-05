from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()

class Gender(models.TextChoices):
   MALE = 'Male', _('Male')
   FEMALE = 'Female', _('Female')
   OTHER = 'Other', _('Other')

class Profile(TimeStampedUUIDModel):
   user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
   phone_number = PhoneNumberField(verbose_name=_('Phone Number'), max_length=15, default='+923041290116')
   about_me = models.TextField(verbose_name=_('About me'), default='say something about yourself')
   license = models.CharField(verbose_name=_('Real Estate License'), max_length=20, null=True, blank=True)
   profile_photo = models.ImageField(verbose_name=_('Profile Photo'), default='/profile_default.png')
   gender = models.CharField(verbose_name=_('Gender'), choices=Gender.choices, default=Gender.MALE, max_length=20)
   country = CountryField(verbose_name=_('Country'), default='PAK', max_length=100, blank=False, null=False)
   city = models.CharField(verbose_name=_('City'), default='Lahore', max_length=100, blank=False, null=False)
   is_buyer = models.BooleanField(verbose_name=_('Buyer'), default=False, help_text=_("Are youlooking to buy a property?"))
   is_seller = models.BooleanField(verbose_name=_('Seller'), default=False, help_text=_('Are you looking to sale property?'))
   is_agent = models.BooleanField(verbose_name=_('Agent'), default=False, help_text=_('Are you an agent?'))
   top_agent = models.BooleanField(verbose_name=_('Top Agent'), default=False)
   rating = models.DecimalField(verbose_name=_('Rating'), max_digits=4, decimal_places=2)
   num_reviews = models.IntegerField(verbose_name=_('Number of Reviews'), default=0, null=True, blank=True)


   def __str__(self):
      return f"{self.user.username}'s profile"

