from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from datetime import datetime
from tinymce.models import HTMLField

class Notice(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, editable=False)
    body = HTMLField()
    date = models.DateField(default=datetime.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title