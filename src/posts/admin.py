from .models import Post
from django.contrib import admin


#Create your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "updated", "timestamp"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
