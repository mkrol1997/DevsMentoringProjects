from django.db import models


class SiteUrlModel(models.Model):
    url = models.URLField(null=False)
