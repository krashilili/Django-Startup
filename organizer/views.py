from django.shortcuts import get_object_or_404, render_to_response
from .models import Tag, Startup
# from django.template import loader
# from django.http.response import HttpResponse


# Create your views here.


def homepage(request):
    tag_list = Tag.objects.all()
    # template = loader.get_template('organizer/tag_list.html')
    # context = {'tag_list':tag_list}
    # output = template.render(context)
    # return HttpResponse(output)
    return render_to_response('organizer/tag_list.html',
                              {'tag_list':tag_list})


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    # template = loader.get_template('organizer/tag_detail.html')
    # context = {'tag': tag}
    # output = template.render(context)
    # return HttpResponse(output)
    return render_to_response('organizer/tag_detail.html',
                              {'tag': tag})


def startup_list(request):
    return render_to_response('organizer/startup_list.html',
                              {'startup_list': Startup.objects.all()})