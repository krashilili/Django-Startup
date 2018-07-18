from django.shortcuts import get_object_or_404, render
from django.views.generic import View
# Create your views here.

from .models import Post


def post_list(request):
    return render(request,
                  'blog/post_list.html',
                  {'post_list': Post.objects.all()})


def post_detail(request, year, month, slug):
    post = get_object_or_404(Post,
                             pub_date__year=year,
                             pub_date__month=month,
                             slug=slug)
    return render(request,
                  'blog/post_detail.html',
                  {'post': post})


class PostList(View):
    """
    Class based view.
    """
    template_name = ''

    def get(self, request):
        return render(request,
                      self.template_name,
                      {'post_list': Post.objects.all()})