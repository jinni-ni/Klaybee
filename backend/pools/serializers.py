from rest_framework import serializers
from externalapi.models import Site

class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = "__all__"
