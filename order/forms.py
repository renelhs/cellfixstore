from django import forms
from .models import Order
from client.models import Client
from product.models import Product
from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('id', )

        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'date_in': forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off',
                                              'readonly': True}),
            'date_out': forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off',
                                               'readonly': True}),
            'imei': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'client': ModelSelect2Widget(model=Client,
                                         queryset=Client.objects.all(),
                                         search_fields=['identification__icontains', 'name_surname__icontains'],
                                         attrs={'data-placeholder': 'Search Client by name or identification',
                                                'style': 'width: 100%'}),
            'service': ModelSelect2MultipleWidget(model=Product,
                                                  search_fields=['code__icontains', 'name__icontains'],
                                                  max_results=50,
                                                  attrs={'data-placeholder':
                                                         'Search Service by name or code',
                                                         'style': 'width: 100%'}),
            'lock_code': forms.TextInput(attrs={'class': 'form-control'}),
            'total_value': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'payment': forms.NumberInput(attrs={'class': 'form-control'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'received_by': forms.Select(attrs={'class': 'form-control'}),
            'delivered_to': forms.TextInput(attrs={'class': 'form-control'}),
            'technician': forms.Select(attrs={'class': 'form-control'}),
            'service_detail': forms.Textarea(attrs={'class': 'form-control',
                                                    'rows': 2}),
            'observations': forms.Textarea(attrs={'class': 'form-control',
                                                  'rows': 2}),
        }
