from django.shortcuts import render
from learning_app.models import Topic, Entry

def index(request):
    """представление главной страницы"""
    return render (request, 'learning_app/index.html')

def topics(request):
    """вывод всех тем"""
    topics = Topic.objects.order_by('date_add')
    context = {'topics' : topics}
    return render(request,'learning_app/topics.html', context)
