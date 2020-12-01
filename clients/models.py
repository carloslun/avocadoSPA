from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Client(models.Model):
    image = models.ImageField(_("Imagen CLiente"), upload_to='client/', height_field=None, width_field=None, max_length=None)
    name = models.CharField(_("Nombre Empresa"), max_length=50)
    description = models.CharField(_("Descripcion"), max_length=100)
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    modified = models.DateTimeField( auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
    