from django.test import TestCase

import unittest
from .models import TagCounter

class TestTagCounter(unittest.TestCase):

    def test_count_tags(self):
        tags = ["<div>", "<div>", "<b>", "<a>", "<a>"]
        tag_counter = TagCounter(tags)
        expected =  { "<div>":2, "<b>":1, "<a>":2 }
        self.assertEquals(expected, tag_counter.count_tags())
