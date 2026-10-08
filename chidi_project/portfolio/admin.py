from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('title', 'post_image_des', 'date',)