from django.urls import path

from news.views import *

urlpatterns = [
    path('', index, name="index"),
    path('topics/', TopicListView.as_view(), name="topic-list"),
    path("topic/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topic/update/<int:pk>/", TopicUpdateView.as_view(), name="topic-update"),
    path("topic/delete/<int:pk>/", TopicDeleteView.as_view(), name="topic-delete"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactor/create/", RedactorCreateView.as_view(), name="redactor-create"),
    path("redactor/update/<int:pk>/", RedactorUpdateView.as_view(), name="redactor-update"),
    path("redactor/delete/<int:pk>/", RedactorDeleteView.as_view(), name="redactor-delete"),
    path("redactor/info/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail")
]

app_name = "news"
