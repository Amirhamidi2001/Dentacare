from django import forms
from .models import Appointment, Contact, Quote, Newsletter


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'


class QuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = '__all__'


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
