from django.db import models
from organizer.models import Startup, Tag
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63, unique_for_month='pub_date', help_text='A label for URL config.')
    text = models.TextField()
    pub_date = models.DateField(verbose_name='date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')

    def __str__(self):
        return f"{self.title} on {self.pub_date.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = 'blog post'


