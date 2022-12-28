from django.contrib import admin
from .models import Memory


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Memory, PostAdmin)
