from django.contrib import admin
from .models import Client

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    # list_display_links = ('pk', 'image')
    # list_editable = ('name',)

    list_filter = ('created', 'modified') 

    # fieldsets = (
    #     ('Profile',{
    #         'fields':(
    #             ('image','title'),
    #             )
    #     }),

    #     ('Extra info',{
    #         'fields':(
    #             ('body'),
    #             # ('biography'),
    #         )
    #     }),

    #     ('Metadata',{
    #         'fields':(
    #             ('created','modified'),
    #             )
    #     }),
    # )
    readonly_fields = ('created','modified')