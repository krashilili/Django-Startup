from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response
# Create your views here.

from .models import Post


def post_list(request):
    return render_to_response('blog/post_list.html',
                              {'post_list': Post.objects.all()})


def post_detail(request, year, month, slug):
    post = get_object_or_404(Post,
                             pub_date__year=year,
                             pub_date__month=month,
                             slug=slug)
    return render_to_response('blog/post_detail.html',
                              {'post': post})