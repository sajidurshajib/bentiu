from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from tinymce.models import HTMLField
from schools.models import Schools

class Courses(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, editable=False)
    body = HTMLField()
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug or (self.pk and self.name != Courses.objects.get(pk=self.pk).name):
            self.slug = slugify(self.name)
            counter = 1
            new_slug = self.slug
            while Courses.objects.filter(slug=new_slug).exists():
                new_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = new_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name