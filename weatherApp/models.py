from django.db import models

class TravelSpot(models.Model):
    region = models.CharField(max_length=50)
    spot_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='travel_spot_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.region} - {self.spot_name}'