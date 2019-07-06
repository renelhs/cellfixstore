from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Client
from .forms import ClientForm
from django.urls import reverse_lazy


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client/client_list.html'
    context_object_name = 'clients'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    # group_required = [u'Jefe de Unidad']
    form_class = ClientForm
    template_name = 'client/client_form.html'
    success_url = reverse_lazy("client:list")


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_form.html'
    success_url = reverse_lazy("client:list")


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client/client_confirm_delete.html'
    success_url = reverse_lazy("client:list")
