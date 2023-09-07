from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=700)
    company = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return '<Article:id=' + str(self.id) + ', ' + \
            self.title + '(' + str(self.date) + '>'

# Create your models here.
