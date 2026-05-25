from django.contrib import admin

from sample.models import Sample

# Register your models here.
@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')