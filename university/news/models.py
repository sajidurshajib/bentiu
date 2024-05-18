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
    # Compress the image to be less than 1MB
    max_size = 1024 * 1024  
    quality = 85
    buffer = BytesIO()
    while True:
        buffer = BytesIO()
        img.save(buffer, format='JPEG', quality=quality)
        if buffer.tell() <= max_size or quality <= 10:
            break
        quality -= 5
        buffer.seek(0)
        img = Image.open(buffer)
    return InMemoryUploadedFile(buffer, None, f"{image.name.split('.')[0]}.jpg", 'image/jpeg', buffer.getbuffer().nbytes, None)

def generate_filename(instance, filename):
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    slug = instance.slug
    filename = f"{slug}_{current_time}.jpg"
    return os.path.join('news', filename)

class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, editable=False)
    body = HTMLField()
    cover = models.ImageField(upload_to=generate_filename)
    date = models.DateField(default=datetime.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        if self.cover:
            self.cover = optimize_and_convert_to_jpg(self.cover)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
