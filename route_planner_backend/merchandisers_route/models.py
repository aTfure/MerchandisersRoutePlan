from django.db import models
from django.contrib.auth.models import User


class RoutePlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route_name = models.CharField(max_length=255)
    date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.route_name} - {self.user.username}"
    
    class Meta:
        ordering = ['-date']
    


class Location(models.Model):
    route_plan = models.ForeignKey(RoutePlan, on_delete=models.CASCADE, related_name='locations')
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Location ({self.latitude}, {self.longitude}) for {self.route_plan.route_name}"
    

    class Meta:
        ordering = ['-timestamp']
