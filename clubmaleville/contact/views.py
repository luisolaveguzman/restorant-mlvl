from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact


class ContactCreateView(CreateView):
    contact = Contact.objects.order_by('id')
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contacto:contacto')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            contact = Contact(
                name=form.cleaned_data.get('name'),
                mail=form.cleaned_data.get('mail'),
                content=form.cleaned_data.get('content')
            )
            contact.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form':form})



