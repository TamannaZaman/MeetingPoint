from django.contrib import admin
from .models import Profile, FriendRequest, Post, Comments, Like, chatMessages

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "image", "slug", "bio")
admin.site.register(Profile, ProfileAdmin)

class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ("to_user", "from_user", "timestamp")
admin.site.register(FriendRequest, FriendRequestAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ("description", "pic", "date_posted", "user_name", "tags")
admin.site.register(Post, PostAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("post", "username", "comment", "comment_date")
admin.site.register(Comments, CommentsAdmin)

class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "post")
admin.site.register(Like, LikeAdmin)

admin.site.register(chatMessages)
