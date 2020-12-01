from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Social(models.Model):
    photo = models.ImageField(_("Fotos"), upload_to='social/', height_field=None, width_field=None, max_length=None)
    title = models.CharField(_("Nombre de la red"), max_length=50)
    url = models.URLField(_("Direccion de la red"), max_length=200)

    def __str__(self):
        return self.title
    
