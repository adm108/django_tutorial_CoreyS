from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # import timezone
    date_posted = models.DateTimeField(default=timezone.now)
    # import User, on_delete - what will happen after deleting User, models.CASCADE - it will delete post also,
    # but if you delete Post it will not delete the User :)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
