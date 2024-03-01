from django.contrib import admin
from .models import *
# Register your models here.
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'size', 'materials', 'painting', 'author')
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'description', 'experience')

admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Author, AuthorAdmin)
