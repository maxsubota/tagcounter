from django.db import models


class PageStatistic(models.Model):
    website = models.URLField()
    source_page = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tag_statistic = models.TextField()

    def __str__(self):
        return '{}'.format(self.website)
