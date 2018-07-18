from django.shortcuts import get_object_or_404, render
from .models import Tag, Startup

# Create your views here.


def tag_list(request):
    tag_list = Tag.objects.all()
    return render(request,
                  'organizer/tag_list.html',
                  {'tag_list':tag_list}
                  )


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    # template = loader.get_template('organizer/tag_detail.html')
    # context = {'tag': tag}
    # output = template.render(context)
    # return HttpResponse(output)
    return render(request,
                  'organizer/tag_detail.html',
                  {'tag': tag})


def startup_list(request):
    return render(request,
                  'organizer/startup_list.html',
                  {'startup_list': Startup.objects.all()})


def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request,
                  'organizer/startup_detail.html',
                  {'startup': startup})