from django.db import models


class Report(models.Model):
    input_file = models.FileField(upload_to='reports_sources')
    output_file = models.FileField(upload_to='reports_ready', null=True, blank=True)
