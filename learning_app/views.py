from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from learning_app.models import Topic, Entry
from learning_app.forms import TopicForm, EntryForm

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

def new_topic(request):
    """ вывод формы для новой темы и обработка """
    if request.method != 'POST':
        form = TopicForm()
    else:
        #если произошел POST запрос(отправили данные); обработка данных
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    return render(request,'learning_app/new_topic.html', context)

def new_entry(request,topic_id):
    """ вывод формы для новой записи по теме и обработка """
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.name_topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'form': form, 'topic': topic}
    return render(request,'learning_app/new_entry.html', context )

def edit_entry(request, entry_id):
    """редактирование старых записей"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.name_topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    context = {'form': form, 'topic': topic, 'entry': entry}
    return render(request,'learning_app/edit_entry.html', context )
