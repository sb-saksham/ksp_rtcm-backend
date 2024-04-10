from django.db import models


def traffic_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / junction_<id>/<direction || filename>
    return 'junction_{0}/{1}'.format(instance.junction.id, instance.direction if instance.direction else filename)


DIRECTION_CHOICES = [
    ('north', 'NORTH'),
    ('south', 'SOUTH'),
    ('east', 'EAST'),
    ('west', 'WEST')
]


class Junction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=264, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class TrafficImage(models.Model):
    junction = models.ForeignKey(Junction, on_delete=models.CASCADE, related_name="traffic_images")
    # which path it is coming North South East West
    direction = models.CharField(choices=DIRECTION_CHOICES, max_length=5, null=True, blank=True)
    image = models.ImageField(upload_to=traffic_directory_path)

    def __str__(self):
        return self.junction.name + '_' + self.direction
