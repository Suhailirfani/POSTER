from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=200, verbose_name="Program Name", blank=True)
    name_image = models.ImageField(upload_to='programs/', blank=True, null=True, verbose_name="Program Name (Image)")
    date = models.DateField()
    place = models.CharField(max_length=200)
    authority = models.CharField(max_length=300, verbose_name="Organising Authority", blank=True)
    authority_image = models.ImageField(upload_to='programs/', blank=True, null=True, verbose_name="Authority (Image)")
    categories = models.CharField(max_length=500, blank=True, verbose_name="Categories (comma separated)")
    teams = models.CharField(max_length=500, blank=True, verbose_name="Teams (comma separated)")

    def __str__(self):
        return f"{self.name} - {self.date}"
