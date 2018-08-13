from django.shortcuts import get_object_or_404, render,redirect
from .models import Tag, Startup
from .forms import TagForm
from django.views.generic import View

# Create your views here.

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
        else:
            return render(
                request,
                'organizer/tag_form.html',
                {'form': form}
            )
    else:
        form=TagForm()
        return render(
            request,
            'organizer/tag_form.html',
            {'form': form}
        )


class TagCreate(View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'

    def get(self, request):
        return render(request,
                      self.template_name,
                      {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)

        else:
            return render(request,
                          self.template_name,
                          {'form': bound_form})



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