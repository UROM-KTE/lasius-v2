import json

from django.core.files.storage import FileSystemStorage
from django.db import models

from .constants import CONTACT_CATEGORIES

logo_storage = FileSystemStorage(location='public_site/logos')


class Contact(models.Model):
    """
    This model contains organizations related to the region's nature protection, rural development, etc.
    """
    category = models.CharField(max_length=100, choices=CONTACT_CATEGORIES)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    logo = models.ImageField(storage=logo_storage, upload_to='media/logos', null=True, blank=True)

    def __str__(self):
        contact_dict = {
            'category': self.category,
            'name': self.name,
            'address': self.address,
            'email': self.email,
            'phone': self.phone,
            'website': self.website,
            'description': self.description,
            'notes': self.notes,
        }
        return json.dumps(contact_dict)

    def get_logo(self):
        return self.logo
