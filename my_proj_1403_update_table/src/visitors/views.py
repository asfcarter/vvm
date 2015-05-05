from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone
from django.core.mail import send_mail


from django.views.generic.detail import DetailView

from django.views.generic.list import ListView

from django.template import RequestContext, loader

from django.shortcuts import render_to_response

from visitors.models import Visitor, Booking

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


from visitors.models import Visitor
from django.views.decorators.csrf import csrf_exempt

class VisitorDetailView(DetailView):
    model = Booking

#    def get_queryset(self, **kwargs):
#        slug = self.kwargs.get('slug') or kwargs.get('slug')
#    if slug:
#        return Visitor.objects.filter(section__slug=slug)
#    else:
#        return Visitor.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VisitorDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    


#class IndexView(generic.ListView):
#    model = Visitor
#    template_name = 'visitors/list.html'
#    context_object_name = 'latest_question_list'
#
#    def get_queryset(self):
#        """Return the last five published questions."""
#        return Visitor.objects[:5]


#class DetailView(generic.DetailView):
#    model = Visitor
#    template_name = 'visitors/details.html'

@csrf_exempt
def booking_table_update(request):
    bookings = Booking.objects.all()
    return render_to_response('visitors/ajax_table.html',{'booking_list' : bookings})

@csrf_exempt
def send_host_request(request):
    host_email = request.POST['host_email']
#    greeted ticked
    send_mail('Hello Andy','Hello worldyyy', 'andy@netfm.org', [host_email],fail_silently=False) 
    bookings = Booking.objects.all()
    return render_to_response('visitors/ajax_table.html',{'booking_list' : bookings})
