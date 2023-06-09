from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # find out what tag is applied to what product
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Generic type of object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # Generic ID of object
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
