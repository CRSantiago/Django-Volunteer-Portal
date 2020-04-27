from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import create_contact_view, ContactDetailView, ContactUpdateView

app_name = 'contacts'
urlpatterns = [
    path('create/', login_required(create_contact_view), name='create-contact-form'),
    path('<int:id>/', login_required(ContactDetailView.as_view()), name='contact-detail'),
    path('<int:id>/update/', login_required(ContactUpdateView.as_view()), name='contact-update'),
]