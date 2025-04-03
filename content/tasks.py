from celery import shared_task
import random
from django.core.cache import cache
from .models import Doha

@shared_task
def refresh_dohas():
    all_dohas = list(Doha.objects.all())
    dohas = random.sample(all_dohas, min(5, len(all_dohas)))  # Pick 5 random Dohas
    cache.set('random_dohas', dohas, 24 * 60 * 60)  # Store for 24 hours
    return "Dohas refreshed successfully"
