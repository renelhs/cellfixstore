import os
from django.shortcuts import render, reverse, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .forms import ConfigurationForm
from .models import Configuration


class ConfigurationUpdateView(LoginRequiredMixin, UpdateView):
    model = Configuration
    form_class = ConfigurationForm
    template_name = 'config/config_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        configuration = Configuration.objects.all()[:1].get()

        try:
            if 'site_logo' in form.changed_data and configuration.site_logo:
                site_logo_dir = configuration.site_logo.path

                if site_logo_dir and os.path.isfile(site_logo_dir):
                    os.remove(site_logo_dir)

            if 'site_logo_mini' in form.changed_data and configuration.site_logo_mini:
                site_logo_mini_dir = configuration.site_logo_mini.path

                if site_logo_mini_dir and os.path.isfile(site_logo_mini_dir):
                    os.remove(site_logo_mini_dir)

        except FileNotFoundError:
            raise Http404

        instance.save()

        return super(ConfigurationUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.method == 'POST':
            return reverse('config:general', kwargs={'pk': self.object.id})
