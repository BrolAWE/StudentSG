from django.contrib import admin

# Register your models here.
from core.models import Participant, Post


@admin.register(Participant)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("last_name",)


@admin.register(Post)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("code",)
