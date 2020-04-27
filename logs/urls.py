from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import create_log_view, hours_total_view ,LogListView, GeneratePdf

app_name = 'logs'
urlpatterns = [
    path('create-log/',login_required(create_log_view), name='log-create-form'),
    path('total-hours/', login_required(hours_total_view), name='hours-total' ),
    path('', login_required(LogListView.as_view()), name='log-list'),
    path('pdf/', login_required(GeneratePdf.as_view()), name='pdf'),
]