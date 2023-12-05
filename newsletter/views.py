# newsletter/views.py
from django.shortcuts import render, redirect
from django.views import View
from .forms import SubscribeForm

class SubscribeView(View):
    template_name = 'newsletter/subscribe.html'

    def get(self, request, *args, **kwargs):
        form = SubscribeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page') 
        return render(request, self.template_name, {'form': form})

class SuccessPageView(View):
    template_name = 'newsletter/success_page.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
