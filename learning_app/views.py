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

def topic(request, topic_id):
    """вывод всех записей одной темы"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_add')
    context = {'topic': topic, 'entries': entries}
    return render(request,'learning_app/topic.html', context)
