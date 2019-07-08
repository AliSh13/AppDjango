from django.shortcuts import render

def index(requst):
    """представление главной страницы"""
    return render (requst, 'learning_app/index.html')
