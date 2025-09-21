from rest_framework import serializers
from .models import ShortURL, Click

class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ["shortcode", "original_url", "expiry", "created_at", "clicks"]

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = "__all__"
