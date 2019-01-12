from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sorl.thumbnail import ImageField

# Create your models here.

class Product(models.Model):
    id = models.SlugField(
        max_length=15,
        unique=True,
        primary_key=True)

    name = models.CharField(
        max_length=150,
        db_index=True, blank=False)

    JANSPORT_CATEGORY = (
        ('big-student', 'Big Student'),
        ('black-label', 'Black Label'),
        ('superbreak', 'Superbreak'),
        ('high-stakes', 'High Stakes'),
        ('digibreak','DigiBreak'),
        ('exposed','Exposed'),
        ('super-fx','Super FX'),
        ('right-pack','Right Pack'),
        ('bento-box','Bento Box')
    )

    BRAND_CHOICES = (
        ('JS', 'Jansport'),
        ('SL', 'Slazenger'),
        ('AL', 'Alentino'),
        ('SS', 'Samsonite'),
        ('HS', 'High Sierra'),
        ('SG', 'Sprayground'),
        ('WI', 'Wilson'),
    )

    TYPE_CHOICES = (
        ('BP', 'Backpack'),
        ('TR', 'Trolley Bag'),
        ('LG', 'Luggage'),
        ('LB', 'Lunch Bag'),
        ('PB', 'Pencil Case'),
        ('TB', 'Tote Bag'),
        ('MB', 'Messenger Bag'),
        ('DF','Duffle Bags'),
    )

    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES)

    brand = models.CharField(
        max_length=2,
        choices=BRAND_CHOICES, blank=False)

    sub_brand = models.CharField(
        max_length=20,
        choices=JANSPORT_CATEGORY,blank=True, null=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2, validators=[MinValueValidator(0.00)]
    )

    image = ImageField(upload_to='store')

    description = models.CharField(
        max_length=150, blank=False)

    in_stock = models.BooleanField(
        default=True, blank=False)

    def __str__(self):
        return self.brand + " " + self.name

#
class Order(models.Model):

    date = models.DateField(
        auto_now_add=True,
    )

    first_name = models.CharField(
        verbose_name="First Name",
        max_length=150,
        blank=False,
    )

    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=150,
        blank=False,
    )
    #
    email = models.EmailField(
        blank=False,
    )

    bag = models.ManyToManyField(
        Product,
        blank=False,
    )

    collection_date = models.DateField(
        blank=False
    )

    paid = models.BooleanField(
        default=False,
        blank=False
    )


    def __str__(self):
        return self.first_name + " " + self.last_name