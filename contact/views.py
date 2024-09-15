from django.urls import reverse_lazy
from django.views.generic import FormView

from . import forms
from . import models


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = forms.ContactForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        models.Contact.objects.create(**form.cleaned_data)
        return super().form_valid(form)
