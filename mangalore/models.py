from django.db import models

# Create your models here.


class Bus(models.Model):
    route_no = models.CharField(max_length = 5)
    stops = models.CharField(max_length = 500)


    def __unicode__(self):
        return self.route_no