from django.db import models


class SiteUrlModel(models.Model):
    url = models.URLField(null=False)

    def __str__(self):
        return f'{self.url}'