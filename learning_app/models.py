from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """ Тема, которую изучает пользователь. """
    name = models.CharField(max_length=200)
    date_add = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    def __str__(self):

        return self.name


class Entry(models.Model):
    """Информация изученная пользователем по теме"""
    name_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_add = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):

        if len(self.text) > 50 :
            return self.text[:50] + '...'

        return self.text
