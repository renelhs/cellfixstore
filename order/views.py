from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from config.models import Configuration
from .forms import OrderForm
from django.urls import reverse_lazy
from django.db.models import Q


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'orders'


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy("order:list")

    def form_valid(self, form):
        last_code = None
        instance = form.save(commit=False)
        configuration = Configuration.objects.all()[:1].get()

        code_exist = Order.objects.filter(
            Q(code=configuration.order_code_sequence))

        if code_exist:
            last_code = Order.objects.order_by('-id')[0].code

        if last_code:
            instance.code = last_code + 1
            configuration.order_code_sequence = last_code + 1
        else:
            instance.code = configuration.order_code_sequence

        instance.save()
        form.save_m2m()
        configuration.save()

        return redirect('order:list')


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy("order:list")


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'order/order_confirm_delete.html'
    success_url = reverse_lazy("order:list")
