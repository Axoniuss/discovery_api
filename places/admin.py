from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        return "No image"

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ['title', 'lng', 'lat']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'image_preview', 'position']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)
        return "No image"