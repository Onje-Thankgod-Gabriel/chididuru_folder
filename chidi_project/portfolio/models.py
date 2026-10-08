from django.db import models
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from datetime import timedelta
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, blank=True, unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # First, create the base slug
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            # Keep checking if slug already exists
            while Blog.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)    
    
    post_image = models.ImageField(upload_to='post_image')
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

    def get_human_date(self):
        now = timezone.now()
        delta = now - self.date

        if delta < timedelta(hours=1):
            mins = int(delta.total_seconds() // 60)
            if mins < 1:
                return "Just now"
            else:
                return f"{mins} min{'s' if mins != 1 else ''} ago"

        elif delta < timedelta(days=1):
            hours = int(delta.total_seconds() // 3600)
            return f"{hours} hour{'s' if hours != 1 else ''} ago"

        elif delta < timedelta(days=30):
            days = delta.days
            return f"{days} day{'s' if days != 1 else ''} ago"

        else:
            # return self.date.strftime("%-d %B %Y")
            return self.date.strftime(f"{self.date.day} %B %Y")  # Explicitly get the day as integer

    def post_image_des(self):
        return mark_safe(f"<img src='{self.post_image.url}' height='40px' width='40px' style='border-radius: 50%;' >")

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title    