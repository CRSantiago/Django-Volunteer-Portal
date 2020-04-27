from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'email',
            'D_O_B',
            'parent_first_name',
            'parent_last_name',
            'parent_cell_phone',
            'school',
            'street',
            'city',
            'state',
            'zipcode',
        ]