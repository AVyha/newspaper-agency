from django.urls import path

from news.views import *

urlpatterns = [
    path('', index, name="index"),
    path('topics/', TopicListView.as_view(), name="topic-list"),
    path("topic/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topic/update/<int:pk>/", TopicUpdateView.as_view(), name="topic-update"),
    path("topic/delete/<int:pk>/", TopicDeleteView.as_view(), name="topic-delete")
]

app_name = "news"
