from django.contrib import admin

from core import models

admin.site.register(models.User)
admin.site.register(models.Category)
admin.site.register(models.Product)
