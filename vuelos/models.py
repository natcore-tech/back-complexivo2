from django.db import models

class Puerta(models.Model):
    code = models.CharField(max_length=10, unique=True)
    terminal = models.CharField(max_length=20, unique=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.code} {self.terminal} {self.is_available} {self.created_at}"


class Estado(models.TextChoices):
        SCHEDULED = "scheduled", "Scheduled"
        BOARDING = "boarding", "Boarding" 
        DEPARTED = "departed", "Departed"
        DELAYED = "delayed", "Delayed"
        CANCELLED = "cancelled", "Cancelled"


class Vuelo(models.Model):
    gate_id = models.ForeignKey(Puerta, on_delete=models.PROTECT, related_name="vuelos")
    flight_number = models.CharField(max_length=20)
    destination = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.SCHEDULED
    )
    departure_time = models.CharField(max_length=60, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.gate_id.code} {self.flight_number} {self.destination} {self.status} {self.departure_time} {self.created_at}"