from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Technician(models.Model):
    tech = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.tech


class Agency(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=True, null=True)
    common_name = models.CharField(max_length=50, unique=True, blank=True, null=True)

    class Meta:
        ordering = ("common_name",)
        verbose_name_plural = "Agencies"

    def __str__(self):
        if self.name:
            return self.name
        return self.common_name


class Zone(models.Model):
    agency = models.ManyToManyField(Agency, related_name="agencies", blank=True)
    name = models.CharField(max_length=50, unique=True)
    common_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    order = models.IntegerField(default=1)
    tech = models.ForeignKey(
        Technician,
        on_delete=models.CASCADE,
        related_name="techs",
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.common_name)
        super(Zone, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail", args=[self.slug])

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.name
