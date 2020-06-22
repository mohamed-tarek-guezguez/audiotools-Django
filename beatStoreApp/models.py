from django.db import models
from ckeditor.fields import RichTextField
import os

from multiselectfield import MultiSelectField

# Create your models here.
class Product(models.Model):
    Title = models.CharField(max_length=250)
    Slug = models.SlugField(unique=True)

    os_choice = (
                ('drumKit', 'Drum Kit'),
                ('midiKit', 'Midi Kit'),
                ('samplePack', 'Loop Kit'),
                ('preset', 'Preset'),
                ('dawPlugin', 'Daw & Plugin'),
                ('tutorial', 'Tutorial'),
    )
    Category = MultiSelectField(choices=os_choice, blank=True, null=True)

    Description = RichTextField(blank=True, null=True)

    Img = models.ImageField(upload_to='pics')

    linkTitle1 = models.CharField(max_length=100, blank=True, null=True)
    link1 = models.URLField(max_length=200, blank=True, null=True)
    linkTitle2 = models.CharField(max_length=100, blank=True, null=True)
    link2 = models.URLField(max_length=220, blank=True, null=True)
    youtubeEmbed = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Title

    def btnColor(self):
        x = self.id
        return x%3

    def snippet(self):
        if len(self.Title) > 33:
            return self.Title[:30] + '...'
        else:
            return self.Title[:33]

class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100, blank=True)
    Message = models.TextField()

    def __str__(self):
        return self.Name
