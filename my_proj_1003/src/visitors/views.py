from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse

from django.template import RequestContext, loader


from visitors.models import Visitor

def index(request):
    return render(request, 'visitors/list.html')

#def index(request):
#    latest_visitor_list = Visitor.objects[:5]
#    context = {'latest_visitor_list': latest_question_list}
#    return render(request, 'visitors/list.html', context)

#def index(request):
#    template = loader.get_template('visitors/list.html')
#    latest_visitor_list = Visitor.objects[:1]
#    latest_visitor_list = {'1','2'}
#    context = RequestContext(request, {
#                'latest_visitor_list': latest_visitor_list,
#                    })
#    return HttpResponse(template.render(context))


class IndexView(generic.ListView):
    model = Visitor
    template_name = 'visitors/list.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Visitor.objects[:5]


class DetailView(generic.DetailView):
    model = Visitor
    template_name = 'visitors/details.html'

