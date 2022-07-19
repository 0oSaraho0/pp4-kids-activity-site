from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Idea(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_ideas")
    updated_on = models.DateTimeField(auto_now=True)
    activity_location = models.CharField(max_length=200, unique=False)
    web_address = models.URLField(max_length=200, default="www.sample.com")
    featured_image = CloudinaryField('image', default='placeholder')
    user_image = models.ImageField(null=True, blank=True)
    content = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='idea_likes', blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    idea = models.ForeignKey(
        Idea, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


# Create your models here.
