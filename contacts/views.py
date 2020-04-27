from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    DetailView,
    UpdateView,
)

from .models import Contact
from .forms import ContactForm

def create_contact_view(request):
    user = request.user
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact_form = form.save(commit=False)
        contact_form.user = request.user
        contact_form.save()
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'contacts/new_contact.html', context)

class ContactDetailView(DetailView):
    template_name = 'contacts/contact_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Contact, id=id_)

class ContactUpdateView(UpdateView):
    template_name = 'contacts/new_contact.html'
    form_class = ContactForm

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Contact, id=id_)
    