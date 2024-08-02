from rest_framework import serializers
from .models import Bengkel, Layanan
from django.contrib.auth.models import User

class LayananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layanan
        fields = ['id', 'nama', 'harga']

class BengkelSerializer(serializers.ModelSerializer):
    layanan = LayananSerializer(many=True, read_only=True)

    class Meta:
        model = Bengkel
        fields = ['id', 'nama', 'alamat', 'deskripsi', 'layanan', 'latitude', 'longitude', 'nomer_hp']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}} 