from django.db import models
from django.utils import timezone
import uuid

class ShortURL(models.Model):
    shortcode = models.CharField(max_length=20, unique=True, db_index=True)
    original_url = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)
    expiry = models.DateTimeField()
    clicks = models.IntegerField(default=0)

    def is_expired(self):
        return timezone.now() > self.expiry

class Click(models.Model):
    shorturl = models.ForeignKey(ShortURL, related_name="clicks_data", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    referrer = models.CharField(max_length=255, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
