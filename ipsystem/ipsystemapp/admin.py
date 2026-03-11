from django.contrib import admin
from django.utils.html import format_html
from .models import CarouselSlide, HeroSection


@admin.register(CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ('order', 'title_line1', 'title_line2_highlight', 'badge_text', 'is_active', 'preview_image')
    list_editable = ('order', 'is_active')
    list_display_links = ('title_line1',)
    ordering = ('order',)
    fieldsets = (
        ('Cài đặt chung', {
            'fields': ('order', 'is_active')
        }),
        ('Badge', {
            'fields': ('badge_icon', 'badge_text')
        }),
        ('Nội dung tiêu đề', {
            'fields': ('title_line1', 'title_line2_highlight', 'description')
        }),
        ('Ảnh nền', {
            'fields': ('image', 'image_url', 'image_alt'),
            'description': 'Upload ảnh hoặc dán URL. Nếu upload ảnh thì để trống URL.'
        }),
        ('Nút bấm', {
            'fields': ('btn1_text', 'btn1_url', 'btn2_text', 'btn2_url')
        }),
    )

    def preview_image(self, obj):
        url = obj.get_image()
        if url:
            return format_html('<img src="{}" style="height:50px;border-radius:6px;" />', url)
        return '—'
    preview_image.short_description = 'Ảnh xem trước'


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title_main', 'title_highlight', 'is_active', 'preview_hero_image')
    fieldsets = (
        ('Cài đặt', {
            'fields': ('is_active',)
        }),
        ('Badge & Tiêu đề', {
            'fields': ('badge_text', 'title_main', 'title_highlight', 'title_suffix', 'description')
        }),
        ('Nút bấm', {
            'fields': ('btn1_text', 'btn1_url', 'btn2_text', 'btn2_url')
        }),
        ('Ảnh Hero (bên phải)', {
            'fields': ('hero_image', 'hero_image_alt'),
            'description': 'Thay ảnh ipsystem_hero.png bằng cách upload tại đây.'
        }),
    )

    def preview_hero_image(self, obj):
        if obj.hero_image:
            return format_html('<img src="{}" style="height:50px;border-radius:6px;" />', obj.hero_image.url)
        return '—'
    preview_hero_image.short_description = 'Ảnh Hero'