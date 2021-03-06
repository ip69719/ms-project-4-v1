from django.db import models

# Create your models here.


class Category(models.Model):
    """ Category model """
    class Meta:
        """ to correct spelling issue """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ String method """
        return self.name

    def get_friendly_name(self):
        """ Model method to return friendly name """
        return self.friendly_name


class Product(models.Model):
    """ Product model """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
