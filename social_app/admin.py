from django.contrib import admin
from social_app.models import Users, Post, Friends

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'fname', 'lname', 'email', 'password','mobile', 'profile_image', 'background_image')

class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'friend', 'user')

admin.site.register(Users, UsersAdmin)
admin.site.register(Post)
admin.site.register(Friends, FriendAdmin)