from django.contrib import admin

# Register your models here.
from .models import Post, Comment


class postModel(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "update"]
    list_filter = ["timestamp", "update"]
    list_per_page = 10
    search_fields = ['title', 'content']

    class Meta:
        model = Post


admin.site.register(Post, postModel)


class CommentModel(admin.ModelAdmin):
    list_display = ["name", "email", "__str__", "post", "time"]
    list_per_page = 20
    search_fields = ['comment', 'name', 'email', 'post']
    list_filter = ["time"]

    class Meta:
        model = Comment


admin.site.register(Comment, CommentModel)
