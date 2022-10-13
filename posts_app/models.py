from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author= models.ForeignKey(User, on_delete= models.CASCADE, related_name='post_pic')
    image = models.ImageField(upload_to ='posted_pic')
    caption = models.CharField(max_length=264)
    upload_date = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering= ['-upload_date']
        
    def __str__(self):
        return self.author
        
class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_post')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='liker')
    
    def __str__(self):
        return self.user