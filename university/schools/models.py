import os
from uuid import uuid4
from datetime import datetime
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from PIL import Image
from io import BytesIO
from tinymce.models import HTMLField
from django.core.files.uploadedfile import InMemoryUploadedFile


def optimize_and_convert_to_jpg(image):
    img = Image.open(image)

    max_size = 1024 * 1024  
    quality = 100
    buffer = BytesIO()

    if buffer.tell() <= 1024 * 1024:
        img.save(buffer, format='JPEG', quality=quality)
        buffer.seek(0)
        return InMemoryUploadedFile(buffer, None, f"{image.name.split('.')[0]}.jpg", 'image/jpeg', buffer.getbuffer().nbytes, None)
    
    while True:
        buffer = BytesIO()
        img.save(buffer, format='JPEG', quality=quality)
        if buffer.tell() <= max_size or quality <= 50:
            break
        quality -= 5
        buffer.seek(0)
        img = Image.open(buffer)
    return InMemoryUploadedFile(buffer, None, f"{image.name.split('.')[0]}.jpg", 'image/jpeg', buffer.getbuffer().nbytes, None)

def generate_filename(instance, filename):
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    slug = instance.slug
    filename = f"{slug}_{current_time}.jpg"
    return os.path.join('schools', filename)

class Schools(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, editable=False)
    body = HTMLField()
    cover = models.ImageField(upload_to=generate_filename)
    position = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        if self.cover:
            self.cover = optimize_and_convert_to_jpg(self.cover)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
