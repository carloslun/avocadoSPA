from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Service(models.Model):
    image = models.ImageField(_("Imagen servicio"), upload_to='service/', height_field=None, width_field=None, max_length=None)
    title = models.CharField(_("Titulo"), max_length=50)
    body = models.TextField(_("Detalles"))
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    modified = models.DateTimeField( auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
    