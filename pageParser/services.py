from service_objects.services import Service
from lxml import html
import requests
import logging
from .models import PageStatistic
import json

logger = logging.getLogger('pageParser.services.PageParserService')

class PageParserService:

    def parse_page(self, page_url):
        self.page = requests.get(page_url)
        tree = html.fromstring(self.page.content)
        return self.collect_tags(tree)

    def collect_tags(self, tree):
        tags = []
        queue = []
        queue.append(tree)
        while(queue):
            node = queue[0]
            queue.remove(node)
            if isinstance(node.tag, str): tags.append(node.tag)
            queue.extend(node.getchildren())
        return tags

class TagCounterService:

    def count_tags_by_url(self, url):
        parser = PageParserService()
        stat = self.count_tags(parser.parse_page(url))
        pagestat = PageStatistic()
        pagestat.website = url
        pagestat.source_page = parser.page.content
        pagestat.tag_statistic = json.dumps(stat)
        pagestat.save()
        logging.info("Saved statistic for " + url)
        return stat

    def count_tags(self, tags):
        tag_statistic = {}

        for tag in set(tags):
            tag_statistic[tag] = sum(1 for t in tags if t == tag)

        return tag_statistic