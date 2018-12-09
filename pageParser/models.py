from django.db import models

class TagCounter:
    def __init__(self, tags):
        self._tags = tags

    @property
    def tags(self):
        return self._tags

    def count_tags(self):
        tag_statistic = {}

        for tag in set(self.tags):
            tag_statistic[tag] = sum(1 for t in self.tags if t == tag)

        return tag_statistic
