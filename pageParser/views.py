from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import WebsiteForm

def index(request):
    return render(request, 'index.html')



class ParserView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        form = WebsiteForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = WebsiteForm(request.POST)
        if form.is_valid():
            website = form.cleaned_data['website']


        args = {'form': form, 'website':website}
        return render(request, self.template_name, args)