from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from news.forms import NewspaperSearchForm
from news.models import Topic, Redactor, Newspaper


def index(request):
    return render(request, "news/index.html")


# Topic CRUD
class TopicListView(generic.ListView):
    model = Topic


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("news:topic-list")


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("news:topic-list")


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("news:topic-list")


# Redactor CRUD
class RedactorListView(generic.ListView):
    model = Redactor


class RedactorCreateView(generic.CreateView):
    model = Redactor
    success_url = reverse_lazy("news:index")
    fields = "__all__"


class RedactorUpdateView(generic.UpdateView):
    model = Redactor
    success_url = reverse_lazy("news:redactor-list")
    fields = "__all__"


class RedactorDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("news:redactor-list")


class RedactorDetailView(generic.DetailView):
    model = Redactor


# Newspapers CRUD
class NewspapersListView(generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspapersListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = NewspaperSearchForm(
            initial={
                "title": title
            }
        )

        return context

    def get_queryset(self):
        title = self.request.GET.get("title")

        if title:
            return self.queryset.filter(title__icontains=title)

        return self.queryset


class NewspapersCreateView(generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("news:newspaper-list")


class NewspaperUpdateView(generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("news:newspaper-list")


class NewspaperDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("news:newspaper-list")


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
