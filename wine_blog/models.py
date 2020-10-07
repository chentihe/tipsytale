from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.
class Variety(models.Model):
    """Model representing a grape variety."""
    name = models.CharField(max_length=100, help_text='Enter a grape variety')
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def save(self, *args, **kwargs): # new
        self.slug = self.slug or slugify(self.name)
        return super().save(*args, **kwargs)

class Country(models.Model):
    """Model representing a country."""
    name = models.CharField(max_length=100, help_text='Enter a country')
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def save(self, *args, **kwargs): # new
        self.slug = self.slug or slugify(self.name)
        return super().save(*args, **kwargs)

class Type(models.Model):
    """Model representing a type."""
    name = models.CharField(max_length=100, help_text='Enter a type')
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def save(self, *args, **kwargs): # new
        self.slug = self.slug or slugify(self.name)
        return super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    variety = models.ManyToManyField(to='Variety', help_text='Select a variety for this wine')
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField(blank=True)
    wine_img = models.ImageField(upload_to='%Y/%m/%d/')
    content = RichTextUploadingField(config_name='my_config', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def display_variety(self):
        """Creates a string for the Variety. This is required to display variety in Admin."""
        return ', '.join([variety.name for variety in self.variety.all()])
    display_variety.short_description = 'Variety'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs): # new
        self.slug = self.slug or slugify(self.title)
        return super().save(*args, **kwargs)