from django.db import models
from django.utils.translation import gettext as _


# Create your models here.

class Contact(models.Model):
    name = models.CharField(_("Nombre:"), max_length=30)
    email = models.EmailField(_("Correo"), max_length=100)
    phone = models.CharField(_("Numero telefonico"), max_length=12)
    message = models.TextField(_("Mensaje"))
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
  

    def __str__(self):
        return self.name
    
