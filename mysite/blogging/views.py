# Views for blogging app

from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Post
from django.views.generic import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    model = Post
    template_name = 'blogging/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(published_date__exact=None).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj is None:
            raise Http404('Post does not exist')
        return obj


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s: %s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


