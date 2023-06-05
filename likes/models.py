from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

# Create your models here.


class LikedItem(models.Model):
    # if a user is deleted, all likes will be deleted as well
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # the type of object the user likes
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # the generic id of that object
    object_id = models.PositiveIntegerField()
    # the actual object liked by the user
    content_object = GenericForeignKey()
