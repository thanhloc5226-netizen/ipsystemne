from django.db import models


class CarouselSlide(models.Model):
    """Quản lý từng slide trong carousel trang chủ"""

    BADGE_ICON_CHOICES = [
        ('developer_mode', 'Developer Mode'),
        ('language', 'Language / Web'),
        ('transform', 'Transform'),
        ('rocket_launch', 'Rocket Launch'),
        ('stars', 'Stars'),
    ]

    order = models.PositiveIntegerField(default=0, verbose_name='Thứ tự hiển thị')
    is_active = models.BooleanField(default=True, verbose_name='Hiển thị')

    # Badge
    badge_icon = models.CharField(
        max_length=50,
        choices=BADGE_ICON_CHOICES,
        default='developer_mode',
        verbose_name='Icon badge'
    )
    badge_text = models.CharField(max_length=100, verbose_name='Chữ badge')

    # Nội dung
    title_line1 = models.CharField(max_length=200, verbose_name='Tiêu đề dòng 1')
    title_line2_highlight = models.CharField(max_length=200, verbose_name='Tiêu đề dòng 2 (màu đỏ)')
    description = models.TextField(verbose_name='Mô tả ngắn')

    # Ảnh nền slide
    image = models.ImageField(
        upload_to='carousel/',
        null=True, blank=True,
        verbose_name='Ảnh nền slide'
    )
    image_url = models.URLField(
        max_length=500, blank=True,
        verbose_name='Hoặc dùng URL ảnh nền',
        help_text='Nếu upload ảnh thì để trống ô này'
    )
    image_alt = models.CharField(max_length=200, default='Slide image', verbose_name='Alt text ảnh')

    # Nút bấm
    btn1_text = models.CharField(max_length=100, verbose_name='Nút 1 - Chữ')
    btn1_url = models.CharField(max_length=200, verbose_name='Nút 1 - URL', help_text="Ví dụ: /contact/ hoặc {% url 'contact:contact' %}")
    btn2_text = models.CharField(max_length=100, verbose_name='Nút 2 - Chữ')
    btn2_url = models.CharField(max_length=200, verbose_name='Nút 2 - URL')

    class Meta:
        ordering = ['order']
        verbose_name = 'Slide Carousel'
        verbose_name_plural = 'Slides Carousel'

    def __str__(self):
        return f"[{self.order}] {self.title_line1} - {self.title_line2_highlight}"

    def get_image(self):
        """Trả về URL ảnh: ưu tiên file upload, sau đó image_url"""
        if self.image:
            return self.image.url
        return self.image_url


class HeroSection(models.Model):
    """Quản lý phần Hero (bên dưới carousel)"""

    is_active = models.BooleanField(default=True, verbose_name='Hiển thị')
    badge_text = models.CharField(max_length=100, default='Chuyên gia giải pháp phần mềm', verbose_name='Chữ badge')
    title_main = models.CharField(max_length=200, default='IPSystem -', verbose_name='Tiêu đề chính')
    title_highlight = models.CharField(max_length=200, default='Chuyên gia', verbose_name='Từ nổi bật (màu đỏ)')
    title_suffix = models.CharField(max_length=200, default='Thiết kế Phần mềm', verbose_name='Phần còn lại của tiêu đề')
    description = models.TextField(verbose_name='Mô tả')

    btn1_text = models.CharField(max_length=100, default='Tư vấn giải pháp', verbose_name='Nút 1 - Chữ')
    btn1_url = models.CharField(max_length=200, default='/contact/', verbose_name='Nút 1 - URL')
    btn2_text = models.CharField(max_length=100, default='Tìm hiểu thêm', verbose_name='Nút 2 - Chữ')
    btn2_url = models.CharField(max_length=200, default='/about/', verbose_name='Nút 2 - URL')

    # Ảnh hero bên phải
    hero_image = models.ImageField(
        upload_to='hero/',
        null=True, blank=True,
        verbose_name='Ảnh hero (bên phải)'
    )
    hero_image_alt = models.CharField(max_length=200, default='Phát triển phần mềm chuyên nghiệp', verbose_name='Alt text ảnh')

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Section'

    def __str__(self):
        return f"Hero: {self.title_main} {self.title_highlight}"