from rest_framework import serializers

from app_pokemon.apps.owner.models import Owner


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('nombre', 'edad', 'pais', 'dni')