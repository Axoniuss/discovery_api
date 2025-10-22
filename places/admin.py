from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ['image_preview', 'image', 'position']  
    readonly_fields = ['image_preview'] 
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px; max-width: 200px;" />', obj.image.url)
        return "No image uploaded"

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'image_preview', 'position']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        return "No image"