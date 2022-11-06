
from rest_framework import serializers
from .models import Identity

class IdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Identity
        fields=('first_name','last_name',)
