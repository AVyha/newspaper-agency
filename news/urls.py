from django.urls import path

from news.views import index

urlpatterns = [
    path('', index)
]

app_name = "news"
