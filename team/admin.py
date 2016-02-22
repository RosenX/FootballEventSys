from django.contrib import admin
from team.models  import *

RegisterClass = (
    Team,
    Player,
    OtherMember
)
for item in RegisterClass:
    admin.site.register(item)
