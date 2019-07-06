import simplejson as json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = reverse_lazy("product:list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = reverse_lazy("product:list")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = reverse_lazy("product:list")


class ProductAjaxView(LoginRequiredMixin, View):
    def get(self, request):
        if request.is_ajax():
            product_id = int(request.GET['product_id'])
            product_obj = Product.objects.get(id=product_id)
            data = json.dumps({'value': product_obj.value})

            return HttpResponse(data, content_type='application/json')
        else:
            raise Http404
