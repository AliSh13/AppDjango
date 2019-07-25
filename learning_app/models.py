from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """ Тема, которую изучает пользователь. """
    name = models.CharField(max_length=200, verbose_name = 'Тема')
    date_add = models.DateField(auto_now_add=True, verbose_name ='Дата добавления')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = 'пользователь' )
    public = models.BooleanField(default=False,verbose_name = 'Публичная')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):

        return self.name


class Entry(models.Model):
    """Информация изученная пользователем по теме"""
    name_topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name = 'Тема')
    text = models.TextField(verbose_name = 'Запись')
    date_add = models.DateField(auto_now_add=True, verbose_name = 'Дата добавления')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):

        if len(self.text) > 50 :
            return self.text[:50] + '...'

        return self.text
