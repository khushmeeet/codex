from django.db import models


class Tags(models.Model):
    tag = models.CharField(max_length=50, unique=True)


class Notes(models.Model):
    BOOK = 'book'
    THOUGHT = 'thought'
    UTILITY = 'utility'
    WEBSITE = 'website'
    RESEARCH_PAPER = 'research_paper'
    PDF = 'pdf'

    SOURCE_TYPE_CHOICES = [
        (BOOK, 'Book'),
        (THOUGHT, 'Thought'),
        (UTILITY, 'Utility'),
        (WEBSITE, 'Website'),
        (RESEARCH_PAPER, 'Research Paper'),
        (PDF, 'PDF')
    ]

    id = models.AutoField(primary_key=True)
    content = models.TextField()
    entity = models.CharField(max_length=500)
    url = models.URLField()
    added_on = models.DateTimeField()
    last_modified_on = models.DateTimeField()
    source_type = models.CharField(max_length=25, choices=SOURCE_TYPE_CHOICES)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
