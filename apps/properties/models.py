import random
import string

from django.db import models
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from apps.common.models import TimeStampedUUIDModel


User = get_user_model()


class PropertyPublishManager(models.Manager):
    def get_queryset(self):
        return (
            super(PropertyPublishManager, self)
            .get_queryset()
            .filter(pusblish_status=True)
            )
        

class Property(TimeStampedUUIDModel):

    class AdvertType(models.TextChoices):
        FOR_SALE = "For Sale", _("For Sale")
        FOR_RENT = "For Rent", _("For Rent")
        FOR_AUCTION = "For Auction", _("For Auction")

    class PropertyType(models.TextChoices):
        HOUSE = "House", _("House")
        APPARTMENMT = "Appartment", _("Appartment")
        OFFICE = "Office", _("Office")
        WAREHOUSE = "Warehouse", _("Warehouse")
        COMMERCIAL = "Commercial", _("Commercial")
        OTHER = "Other", _("Other")

    user = models.ForeignKey(User, verbose_name=_("Agent,Seller or Buyer"), on_delete=models.DO_NOTHING, related_name="agent_buyer")
    title = models.CharField(verbose_name=_("Property Title"), max_length=250)
    slug = AutoSlugField(populate_from ="title", unique=True, always_update=True)
    ref_code = models.CharField(verbose_name=_("Property Reference"), unique=True, max_length=255, blank=True)
    description = models.TextField(verbose_name=_("Description"), default="Please Enter Description")
    country = CountryField(verbose_name=_("Country"), default="PK", blank_label="Select Country")
    city = models.CharField(verbose_name=_("city"), default="Lahore", max_length=100)
    postal_code = models.CharField(verbose_name=_("Postal Code"), max_length=100, default=58810)
    street_address = models.CharField(verbose_name=_("Street Address"), max_length=255, default="Airport Road")
    property_number = models.IntegerField(verbose_name=_("Property Number"), validators=[MinValueValidator(1)])
    price = models.DecimalField(verbose_name=_("Property Price"), default=0.0, max_digits=8, decimal_places=2)
    tax = models.DecimalField(verbose_name=_("Property Tax"), default=0.15, help_text="15% OF Property Price", max_digits=6, decimal_places=2)
    plot_area = models.DecimalField(verbose_name=_("Property Area(m**2)"), max_digits=8, decimal_places=2, default=0.0)
    total_floors = models.IntegerField(verbose_name=_("Total Floors"), default=1)
    bedrooms = models.IntegerField(verbose_name=_("Total Bedrooms"), default=1)
    bathrooms = models.DecimalField(verbose_name=_("Total Bathrooms"), max_digits=6, decimal_places=1, default=1.0)
    advert_type = models.CharField(verbose_name=_("Advertise Type"), max_length=50, choices=AdvertType.choices, default=AdvertType.FOR_SALE)
    property_type = models.CharField(verbose_name=_("Property Type"), choices=PropertyType.choices, default=PropertyType.HOUSE)
    cover_photo = models.ImageField(verbose_name=_("Mian Photo"), default="/house_photo.png", null=True, blank=True)
    photo1 = models.ImageField(verbose_name=_("Mian Photo"), default="/house_photo.png", null=True, blank=True)
    photo2 = models.ImageField(verbose_name=_("Mian Photo"), default="/house_photo.png", null=True, blank=True)
    photo3 = models.ImageField(verbose_name=_("Mian Photo"), default="/house_photo.png", null=True, blank=True)
    photo4 = models.ImageField(verbose_name=_("Mian Photo"), default="/house_photo.png", null=True, blank=True)
    published_status = models.BooleanField(verbose_name=_("Published Status"), default=False)
    views = models.IntegerField(verbose_name=_("Total Views"), default=0)

    objects = models.Manager()
    published = PropertyPublishManager()

    def __str__(self):
        return self.title()
    
    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def save(self, *args, **kwargs):
        self.title = str.title(self.title)
        self.description = str.title(self.description)
        self.ref_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
        super(Property, self).save(*args, **kwargs)

    @property
    def final_property_price(self):
        tax_percentage = self.tax
        property_price  =self.price
        tax_amount = round(tax_percentage * property_price, 2)
        price_after_tax = float(round(tax_amount + property_price, 2))
        return price_after_tax



class PropertyViews(TimeStampedUUIDModel):
    ip = models.CharField(verbose_name=_("IP Address"), max_length=50)
    property = models.ForeignKey(Property, related_name='property_views' ,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Total Views on - {self.property.title} is - {self.property.views} view(s)"
    
    class Meta:
        verbose_name = "Total Property Views"
        verbose_name_plural = "Total Property Views"