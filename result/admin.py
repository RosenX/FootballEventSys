from django.contrib import admin
from result.models  import *

RegisterClass = (
    Score,
    RedCard,
    YellowCard,
    SumScore,
    RedCardReason,
    YellowCardReason,
)
for item in RegisterClass:
    admin.site.register(item)
