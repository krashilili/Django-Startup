from django.db import models
from django.urls import reverse

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config.')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organizer_tag_detail', kwargs={'slug': self.slug})

    class Meta:
        """
        Order the Tag model alphabetically by the name field.
        """
        ordering = ['name']


class Startup(models.Model):
    name = models.CharField(max_length=31, db_index=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config.')
    description = models.TextField()
    founded_date = models.DateField(verbose_name='data founded')
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organizer_startup_detail',
                       kwargs={'slug': self.slug})

    class Meta:
        """
        Order the lists of Startup objects by name and the latest object should be with the most recent
        founded_date field.
        """
        ordering = ['name']
        get_latest_by = 'founded_date'


class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField(verbose_name='date published')
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.startup}: {self.title}"

    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

