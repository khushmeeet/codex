from django.db import models


class ExternalData(models.Model):
    HTML = 'HTML'
    PDF = 'PDF'

    DATA_TYPE_CHOICES = [
        (HTML, 'HTML'),
        (PDF, 'PDF')
    ]

    id = models.AutoField(primary_key=True)
    content = models.TextField()
    url = models.URLField()
    added_on = models.DateTimeField()
    data_type = models.CharField(max_length=50, choices=DATA_TYPE_CHOICES)
