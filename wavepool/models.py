from django.db import models
from django.urls import reverse
from django.shortcuts import redirect
from urllib.parse import urlparse
from django.utils import timezone

DIVESITE_SOURCE_NAMES = {
    'retaildive': 'Retail Dive',
    'ciodive': 'CIO Dive',
    'educationdive': 'Education Dive',
    'supplychaindive': 'Supply Chain Dive',
    'restaurantdive': 'Restaurant Dive',
    'grocerydive': 'Grocery Dive',
    'biopharmadive': 'BioPharma Dive',
    'hrdive': 'HR Dive',
}


class NewsPost(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=3000)
    source = models.URLField(unique=True)
    is_cover_story = models.BooleanField(default=False)
    publish_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def clean(self):
        if self.is_cover_story == True:
            if NewsPost.objects.filter(is_cover_story=True).exists():
                original = NewsPost.objects.filter(is_cover_story=True).get()
                original.is_cover_story = False
                original.save()

    
    @property
    def url(self):
        return reverse('newspost_detail', kwargs={'newspost_id': self.pk})

    @property
    def teaser(self):
        return self.body[:150]

    @property
    def source_divesite_name(self):
        url = urlparse(self.source)
        return DIVESITE_SOURCE_NAMES["{}".format(url.netloc[4:-4])]

    def tags(self):
        return [
            'HR', 'Diversity & Inclusion', 'Culture'
        ]
