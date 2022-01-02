from django.db import models


class Post(models.Model):
    post_slug = models.SlugField(db_index=True, max_length=255, unique=True)
    post_title = models.CharField(db_index=True, max_length=255)

    post_description = models.TextField()
    post_body = models.TextField()

    post_created = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now=True)

# Create your models here.
