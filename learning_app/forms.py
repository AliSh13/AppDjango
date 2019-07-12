from django import forms

from learning_app.models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Форма новой темы """
    class Meta:
        model = Topic
        fields = ['name']
        labels = {'name':''}
