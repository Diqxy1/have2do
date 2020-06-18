from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

    @property
    def abstract(self):
        return '{}...'.format(self.description[:40])
