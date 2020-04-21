from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import (
    DetailView,
    ListView,
    View,
)



from datetime import date

from .models import Log
from .forms import LogForm
from .utils import render_to_pdf

def create_log_view(request):
    user = request.user
    form = LogForm(request.POST or None)
    if form.is_valid():
        log_form = form.save(commit=False)
        log_form.user = request.user
        log_form.save()
        form = LogForm

    context = {
        'form': form
    }

    return render(request, 'logs/new_log.html', context)

def hours_total_view(request):
    hours_total = 0
    for h in Log.objects.raw("SELECT * FROM logs_log WHERE user_id = %s", [request.user.id]):
        hours_total += h.hours_completed

    context = {
        'hours_total':hours_total
    }
    return render(request, 'logs/log_total.html', context)

class LogListView(ListView):
    template_name = 'logs/log_list.html'
    queryset = Log.objects.all()

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        hours_total = 0
        for h in Log.objects.raw("SELECT * FROM logs_log WHERE user_id = %s", [request.user.id]):
            hours_total += h.hours_completed

        context = {
            'date': date.today(),
            'firstname':request.user.first_name,
            'lastname': request.user.last_name,
            'hours_total':hours_total
        }
        pdf = render_to_pdf('logs/hours_request.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
