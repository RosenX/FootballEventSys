from django.contrib import admin
from event.models  import *

RegisterClass = (
    SingleMatch,
    Schedule,
    Event,
)
for item in RegisterClass:
    admin.site.register(item)
