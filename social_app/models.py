from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class ActivityTracking(models.Model):
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Users(ActivityTracking):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    mobile = models.BigIntegerField(null=False, blank=False, unique=True)
    password = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='Profile_image/%Y/%m/%d', blank=True, null=True)
    background_image = models.ImageField(upload_to='Profile_image/%Y/%m/%d', blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    relationship = models.BooleanField(default=False)
    is_friend = models.BooleanField(default=False)
    is_mutual = models.BooleanField(default=False)
    is_married = models.BooleanField(default=False)

    def __str__(self):
        return self.fname

class Friends(ActivityTracking):    
    friend = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='friend_id')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_session_id')

    def __str__(self):
        return str(self.friend)

class Post(ActivityTracking):
    title = RichTextField() 
    posts = RichTextUploadingField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return self.user.fname











