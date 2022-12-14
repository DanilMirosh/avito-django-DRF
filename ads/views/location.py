from rest_framework.viewsets import ModelViewSet

from ads.models import Location
from ads.serializers.location import LocationSerializer


class LocationViewSet(ModelViewSet):
    """Viewset for location model"""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
