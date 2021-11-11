from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.utils.timezone import now
#from home.views import blogpost

# Create your models here.
class BlogPost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    blogthumb = models.ImageField(upload_to ='static/images/')
    author = models.CharField(max_length=40)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(blank=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name="liked")

    def __str__(self):
        return self.title + 'By' + self.author 
    @property
    def num_likes(self):
        return self.liked.all().count()



class SearchQuery(models.Model):

    searchValue = models.TextField()

    def __str__(self):
        return self.searchValue


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    parent = models.ForeignKey("self",on_delete=models.CASCADE, null=True)
    timeStamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:13] + '....'+ ' By ' + self.user.username

LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)