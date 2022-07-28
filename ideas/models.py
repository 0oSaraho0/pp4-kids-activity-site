from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Idea(models.Model):
    """ A model to create Idea items """

    COST = [('free', 'Free'),
            ('10', 'Under £10 per person'),
            ('20', 'Under £20 per person'),
            ('30', 'Under £30 per person'),
            ('40', 'Under £40 per person'),
            ('50', 'Under £50 per person'),
            ('50+', 'Over £50 per person')
            ]

    AGE_RANGE = [
        ('all_ages', 'All Ages'),
        ('u1', 'Under 1'),
        ('1-2', '1 to 2 Years'),
        ('2-3', '2 to 3 Years'),
        ('3-5', '3 to 5 Years'),
        ('6-8', '6 to 8 Years'),
        ('9-11', '9 to 11 Years'),
        ('12-14', '12 to 14 Years'),
        ('15-17', '15 to 17 years'),
        ('u5', 'Under 5s'),
        ('u10', 'Under 10s'),
        ('o10', 'Over 10s')
    ]

    activity_name = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_ideas")
    updated_on = models.DateTimeField(auto_now=True)
    activity_location = models.CharField(max_length=200, unique=False)
    activity_website = models.URLField(
        max_length=200, blank=True)
    picture = CloudinaryField('image', default='placeholder')
    cost = models.CharField(max_length=200, choices=COST, default='free')
    age_range = models.CharField(
        max_length=200, choices=AGE_RANGE, default='all_ages')
    review = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='idea_likes', blank=True)

    class Meta:
        """ Order by Activity Name """
        ordering = ['activity_name']

    def __str__(self):
        return self.activity_name

    def number_of_likes(self):
        """ A function to count the number of likes """
        return self.likes.count()


class Comment(models.Model):
    """ A model to make a comment """
    idea = models.ForeignKey(
        Idea, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ Order by created on date """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
