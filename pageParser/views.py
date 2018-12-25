from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import WebsiteForm
import validators
from pageParser.services import TagCounterService
from urllib.request import urlopen, URLError

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

        if validators.url(website) and self.check_url_connection(website):
            tagcounter = TagCounterService()
            tag_statistic = tagcounter.count_tags_by_url(website)
            args = {'form': form, 'website':website, 'tag_statistic': tag_statistic}
        else:
            args = {'form': form, 'error_message': 'Website URL is invalid'}

        return render(request, self.template_name, args)

    def check_url_connection(self, url):
        try:
            urlopen(url)
            return True
        except URLError:
            return True