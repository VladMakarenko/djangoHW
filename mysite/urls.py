
from django.contrib import admin
from django.urls import path
from myapp.views import main, articles, users, article, archive

urlpatterns = [
    path('', main),
    path('articles/', articles),
    path('articles/archive/', archive),
    path('users/', users),
    path('article/<int:article_number>/', article),
    path('article/<int:article_number>/archive/', article),
    path('article/<int:article_number>/<slug:slug_text>/',article),
    path('users/<int:user_number>', users),
]
