from django.test import TestCase

from .services import TagCounterService
from .services import PageParserService


class TestTagCounter(TestCase):
    def test_count_tags(self):
        tags = ["<div>", "<div>", "<b>", "<a>", "<a>"]
        tag_counter = TagCounterService()
        expected = {"<div>": 2, "<b>": 1, "<a>": 2}
        self.assertEquals(expected, tag_counter.count_tags(tags))

    def test_count_tags2(self):
        parser = PageParserService()
        tags = parser.parse_page("http://econpy.pythonanywhere.com/ex/001.html")
        tag_counter = TagCounterService()
        tag_statistic = tag_counter.count_tags(tags)
        self.assertTrue(len(tag_statistic) > 0)


class TestPageParserService(TestCase):
    def test_parse_page(self):
        parser = PageParserService()
        tags = parser.parse_page("http://onliner.by")
        self.assertTrue(len(tags) > 0)
