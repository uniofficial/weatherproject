from django.db import models

class TravelSpot(models.Model):
    region = models.CharField(max_length=50)
    spot_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.region} - {self.spot_name}'
