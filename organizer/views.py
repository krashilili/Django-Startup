from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Tag
from django.template import loader
from django.template import Template, Context

# Create your views here.


def homepage(request):
    tag_list = Tag.objects.all()
    # output = ", ".join([tag.name for tag in tag_list])
    template = loader.get_template('organizer/tag_detail.html')
    context = Context({'tag':tag_list})
    output = template.render({'tag':tag_list[0]})
    # output = ", ".join([tag.name for tag in tag_list])
    return HttpResponse(output)