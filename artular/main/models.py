from django.db import models
import uuid




def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'pictures/{new_file_name}'

class Author(models.Model):
    author_name = models.CharField(max_length = 100)
    description = models.TextField()
    experience = models.TextField()
    def __str__(self):
        return self.author_name

class Artwork(models.Model):
    name = models.CharField(max_length = 100)
    size = models.CharField(max_length = 50)
    materials = models.CharField(max_length = 50)
    painting = models.ImageField(blank=True, null=True, upload_to=uniq_name_upload)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

