from django.db import models

# Create your models here.
class Task:
    def __init__(self, title, description, image):
        self.title = title
        self.description = description
        self.image = image

    @property
    def abstract(self):
        return '{}...'.format(self.description[:50])
