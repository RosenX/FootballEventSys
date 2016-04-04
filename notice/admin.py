from django.contrib import admin
from notice.models  import *

RegisterClass = (
    Notice,
)
for item in RegisterClass:
    admin.site.register(item)
