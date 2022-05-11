from django.contrib.gis.db import models


class Points(models.Model):
    point = models.PointField()
