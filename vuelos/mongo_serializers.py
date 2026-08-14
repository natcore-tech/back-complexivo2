from rest_framework import serializers

class AirlineTypeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    code = serializers.CharField(required=False, allow_blank=True)
    country = serializers.CharField(required=False)
    is_active = serializers.BooleanField(default=True)
    created_at = serializers.DateTimeField(required=False)

class Estado:
        CREATED = "created"
        BOARDING_STARTED = "boarding_started"
        DEPARTED = "departed"
        DELAYED = "delayed"
        CANCELLED = "cancelled"

        CHOICES = [
            (CREATED, "Created"),
            (BOARDING_STARTED, "Boardign_started"),
            (DEPARTED, "Departed"),
            (DELAYED, "Delayed"),
            (CANCELLED, "Cancelled"),
        ]

class Estado2:

        WEB = "web"
        MOBILE = "mobile"
        SYSTEM = "system"

        CHOICES = [
            (WEB, "Web"),
            (MOBILE, "Mobile"),
            (SYSTEM, "System"),
        ]

class VueloServiceSerializer(serializers.Serializer):
    flight_id = serializers.IntegerField()        # ID de Vehiculo (Postgres)
    

    event_type = serializers.ChoiceField(
        choices=Estado.CHOICES,
        default=Estado.CREATED
    )

    source string = serializers.ChoiceField(
        choices=Estado2.CHOICES,
        default=Estado2.WEB
    )

    note = serializers.CharField()       # ObjectId (string) de service_types
    created_at = serializers.DateTimeField(required=False)