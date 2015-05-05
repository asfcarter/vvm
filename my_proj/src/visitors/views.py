from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone

from django.views.decorators.csrf import csrf_exempt


from django.views.generic.detail import DetailView

from django.views.generic.list import ListView

from django.template import RequestContext, loader


from visitors.models import Visitor, Booking, BookingForm
#from visitors.models import Visitor

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render
from django.shortcuts import render_to_response

#def index(request):
#    return render(request, 'visitors/list.html')

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


def add_booking(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('/Vodafone/visitors/add_booking/')
    else:
        form = BookingForm()

        return render(request, 'add_booking.html', {'form': form})

class VisitorListView(ListView):
    model = Visitor

#    some_params= 'test'
#    msg_plain = render_to_string('/home/dave/vvm/my_proj/src/templates/booking_email.txt', {'some_params': some_params})
#    msg_html = render_to_string('/home/dave/vvm/my_proj/src/templates/booking_email.html', {'some_params': some_params})
#
#    send_mail('Visitor Booking for Vodafone', msg_plain, 'dave@netfm.org',
#                ['dave@netfm.org'], html_message=msg_html, fail_silently=False)


class VisitorDetailView(DetailView):
    model = Visitor

#    send_mail('Subject here', 'Here is the message.', 'dave@netfm.org',
#                ['dave@netfm.org'], fail_silently=False)

    def get_context_data(self, **kwargs):
        context = super(VisitorDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


@csrf_exempt
def update_anpr(request):
    booking = request.POST['booking']
    booking.anpr = True 
    booking.save()
    return


@csrf_exempt
def booking_table_update(request):
    bookings = Booking.objects.all()
    return render_to_response('visitors/ajax_table.html',{'booking_list' : bookings})


@csrf_exempt
def send_host_request(request):
    host_email = request.POST['host_email']
    bookings = Booking.objects.all()
    some_params= 'test'
    msg_plain = render_to_string('/home/dave/vvm/my_proj/src/templates/booking_email.txt', {'some_params': some_params})
    msg_html = render_to_string('/home/dave/vvm/my_proj/src/templates/booking_email.html', {'some_params': some_params})

    send_mail('Visitor Booking for Vodafone', msg_plain, 'dave@netfm.org',
            [host_email], html_message=msg_html, fail_silently=False)

    return render_to_response('visitors/ajax_table.html',{'booking_list' : bookings})


