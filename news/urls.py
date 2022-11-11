from django.urls import path

from news.views import *

urlpatterns = [
    path('', index, name="index"),
    path('topics/', TopicListView.as_view(), name="topic-list"),
    path("topic/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topic/update/<int:pk>/", TopicUpdateView.as_view(), name="topic-update"),
    path("topic/delete/<int:pk>/", TopicDeleteView.as_view(), name="topic-delete"),
    path("topic/detail/<int:pk>/", TopicDetailView.as_view(), name="topic-detail"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactor/create/", RedactorCreateView.as_view(), name="redactor-create"),
    path("redactor/update/<int:pk>/", RedactorUpdateView.as_view(), name="redactor-update"),
    path("redactor/delete/<int:pk>/", RedactorDeleteView.as_view(), name="redactor-delete"),
    path("redactor/info/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path("newspapers/", NewspapersListView.as_view(), name="newspaper-list"),
    path("newspaper/create/", NewspapersCreateView.as_view(), name="newspaper-create"),
    path("newspaper/update/<int:pk>/", NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("newspaper/detail/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspaper/delete/<int:pk>/", NewspaperDeleteView.as_view(), name="newspaper-delete")
]

app_name = "news"
