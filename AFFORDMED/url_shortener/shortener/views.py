from django.shortcuts import redirect
from django.utils import timezone
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import ShortURL, Click
from .serializers import ShortURLSerializer
from .utils import generate_shortcode
import datetime

@api_view(["POST"])
def create_shorturl(request):
    url = request.data.get("url")
    validity = int(request.data.get("validity", 30))  # minutes
    shortcode = request.data.get("shortcode")

    if not shortcode:
        shortcode = generate_shortcode()

    expiry_time = timezone.now() + datetime.timedelta(minutes=validity)

    shorturl = ShortURL.objects.create(
        original_url=url,
        shortcode=shortcode,
        expiry=expiry_time
    )

    response = {
        "shortLink": f"http://localhost:8000/{shortcode}",
        "expiry": expiry_time
    }
    return JsonResponse(response, status=201)


def redirect_shorturl(request, shortcode):
    try:
        shorturl = ShortURL.objects.get(shortcode=shortcode)
        if shorturl.is_expired():
            return JsonResponse({"error": "URL expired"}, status=410)

        shorturl.clicks += 1
        shorturl.save()

        Click.objects.create(
            shorturl=shorturl,
            referrer=request.META.get("HTTP_REFERER"),
            ip_address=request.META.get("REMOTE_ADDR"),
            user_agent=request.META.get("HTTP_USER_AGENT")
        )
        return redirect(shorturl.original_url)

    except ShortURL.DoesNotExist:
        return JsonResponse({"error": "Shortcode not found"}, status=404)


@api_view(["GET"])
def stats_shorturl(request, shortcode):
    try:
        shorturl = ShortURL.objects.get(shortcode=shortcode)
        serializer = ShortURLSerializer(shorturl)
        click_data = [
            {
                "timestamp": c.timestamp,
                "referrer": c.referrer,
                "ip": c.ip_address,
                "ua": c.user_agent
            }
            for c in shorturl.clicks_data.all()
        ]
        return JsonResponse({
            "url": serializer.data,
            "clicks": click_data
        }, safe=False)

    except ShortURL.DoesNotExist:
        return JsonResponse({"error": "Shortcode not found"}, status=404)
