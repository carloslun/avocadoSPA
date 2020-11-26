from django.contrib import admin
from .models import Service

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('created', 'modified', 'title')
    # list_display_links = ('pk', 'image')
    list_editable = ('title',)

    list_filter = ('created', 'modified') 

    fieldsets = (
        ('Profile',{
            'fields':(
                ('image','title'),
                )
        }),

        ('Extra info',{
            'fields':(
                ('body'),
                # ('biography'),
            )
        }),

        ('Metadata',{
            'fields':(
                ('created','modified'),
                )
        }),
    )
    readonly_fields = ('created','modified')

