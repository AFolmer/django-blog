# Views for blogging app

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Post


def list_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blogging/list.html', context)


def detail_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {'post': post}
    return render(request, 'blogging/detail.html', context)


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s: %s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


