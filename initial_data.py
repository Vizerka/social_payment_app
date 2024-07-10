# initial_data.py

import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from frontend.models import Benefit

initial_benefits = [
    "Grusza",
    "Zapomoga",
    "Refundacja",
    "Pożyczka mieszkaniowa",
    "Wycieczka"
]

for benefit_name in initial_benefits:
    Benefit.objects.get_or_create(name=benefit_name)

print("Initial data loaded successfully.")