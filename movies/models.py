from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):

    CATEGORY_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Horror', 'Horror'),
        ('Drama', 'Drama'),
        ('Sci-Fi','Sci-Fi'),
        ('Fantasy','Fantasy'),
        ('Romance','Romance')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50,
                                choices=CATEGORY_CHOICES)

    thumbnail = models.ImageField(upload_to='thumbnails/')
    video = models.FileField(upload_to='videos/')

    uploaded_by = models.ForeignKey(User,
                                    on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
from django.contrib.auth.models import User

class ViewHistory(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    watched_at = models.DateTimeField(
        auto_now_add=True
    )

