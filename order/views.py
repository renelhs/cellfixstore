from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from config.models import Configuration
from .forms import OrderForm
from django.urls import reverse_lazy
from django.db.models import Q
from dateutil.relativedelta import relativedelta
from calendar import monthrange
from datetime import datetime


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'order/dashboard.html'

    def get_value(self, q_date_from, q_date_to, q_type):
        query_result = Order.objects.filter(Q(date_in__range=(q_date_from, q_date_to)), state__exact='delivered')

        if q_type == 'o':
            return len(query_result) or 0
        else:
            total_value = 0

            if query_result:
                for x in query_result:
                    total_value += int(x.total_value) or 0

            return total_value

    def get_graphics_data(self):
        graphics_data = []

        start_date = datetime.today()
        months_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
                        8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

        for i in range(12):
            last_day = monthrange(start_date.year, start_date.month)[1]
            month_orders = self.get_value(start_date.replace(day=1).strftime("%Y-%m-%d"),
                                          start_date.replace(day=last_day).strftime("%Y-%m-%d"), 'o')
            month_incomes = self.get_value(start_date.replace(day=1).strftime("%Y-%m-%d"),
                                           start_date.replace(day=last_day).strftime("%Y-%m-%d"), 'i')
            graphics_data.append((months_names[start_date.month] + ' ' + str(start_date.year),
                                  month_orders, month_incomes))
            start_date += relativedelta(months=-1)

        return graphics_data

    def get_context_data(self, **kwargs):
        labels = []
        month_orders = []
        month_incomes = []
        context = super(DashboardView, self).get_context_data(**kwargs)

        for i in reversed(self.get_graphics_data()):
            labels.append(i[0])
            month_orders.append(i[1])
            month_incomes.append(i[2])

        context['labels'] = labels
        context['month_orders'] = month_orders
        context['month_incomes'] = month_incomes

        return context


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
