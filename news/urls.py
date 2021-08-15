from django.contrib import admin
from django.urls import path
from .views import NewsCreateListView, NewsDetailGenericView


urlpatterns = [
    path('news/', NewsCreateListView.as_view()),
    path('news_detailed/<int:id>/', NewsDetailGenericView.as_view()),

]