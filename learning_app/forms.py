from django import forms

from learning_app.models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Форма новой темы """
    class Meta:
        model = Topic
        fields = ['name', 'public']
        labels = {'text':'','public': 'Публичная'}

class EntryForm(forms.ModelForm):
    """Форма создания записи по теме"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        #изменяем ширину ввода текстового поля
        widgets = {'text': forms.Textarea(attrs={'colos': 80})}
