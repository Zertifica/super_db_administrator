from api.models.connection import ConnectionDb
from rest_framework import serializers

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionDb
        fields = ('name', 'db_name', 'host', 'port', 'password', 'username')
