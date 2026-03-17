
from django.shortcuts import render
from .models import CarouselSlide, HeroSection
from portfolio.models import *
import json
from groq import Groq
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

groq_client = Groq(api_key=settings.GROQ_API_KEY)

# Create your views here.


def home(request):
    slides = CarouselSlide.objects.filter(is_active=True).order_by('order')
    hero = HeroSection.objects.filter(is_active=True).first()
    portfolio = Portfolio.objects.all()

    context = {
        'slides': slides,
        'hero': hero,
        'portfolio': portfolio,
        'title': 'Trang chủ',
    }
    return render(request, 'ipsystemapp/home.html', context)


# AI Chatbox
def get_site_data():
    from ipsystemapp.models import HeroSection  # thay đúng tên app
    from portfolio.models import Portfolio, Category
    from service.models import Service
    
    # Hero section
    hero = HeroSection.objects.filter(is_active=True).first()
    hero_text = ""
    if hero:
        hero_text = f"""
Giới thiệu công ty:
- Tên: {hero.title_main} {hero.title_highlight} {hero.title_suffix}
- Mô tả: {hero.description}
- Liên hệ tư vấn: {hero.btn1_url}
"""

    service_text = """
IPSystem cung cấp 4 loại dịch vụ thiết kế website/phần mềm:

1. Website Giới thiệu Doanh nghiệp
   Thiết kế website chuyên nghiệp, hiện đại phản ánh đúng giá trị thương hiệu.

2. Website Thương mại điện tử
   Xây dựng hệ thống mua sắm trực tuyến mạnh mẽ, tối ưu chuyển đổi và trải nghiệm mua hàng.

3. Hệ thống quản lý nội bộ
   Phát triển ERP, CRM và các hệ thống nội bộ tối ưu hóa vận hành doanh nghiệp.

4. Phần mềm khác theo yêu cầu
   Phát triển phần mềm theo nhu cầu thiết yếu của thị trường và doanh nghiệp.

Khi khách hỏi IPSystem làm gì, hãy liệt kê đúng 4 loại trên.
"""

    # Portfolio / dự án
    portfolios = Portfolio.objects.select_related('category').all()
    portfolio_text = "\nDự án đã thực hiện:\n"
    for p in portfolios:
        portfolio_text += f"- [{p.category.name}] {p.title}: {p.description}\n"
        if p.achievements:
            portfolio_text += f"  Kết quả: {p.achievements}\n"
        if p.url:
            portfolio_text += f"  Link: {p.url}\n"
            
    pricing_text = """
Bảng giá dịch vụ thiết kế website:

- Gói BASIC: 5 triệu đồng
  Phù hợp cho cá nhân hoặc doanh nghiệp mới khởi nghiệp
  + Miễn phí tên miền 1 năm
  + Tối ưu tốc độ & Bảo mật SSL
  + Tích hợp Mạng xã hội
  + Bảo hành 6 tháng
  - Không bao gồm: Viết bài & Nội dung, Thiết kế UI/UX riêng biệt

- Gói STANDARD: 8 - 12 triệu đồng (Phổ biến nhất)
  Giải pháp hoàn hảo cho doanh nghiệp vừa và nhỏ
  + Mọi tính năng gói Basic
  + Viết bài & Nội dung cơ bản
  + Thiết kế UI/UX tùy chỉnh
  + Hỗ trợ viết bài & nội dung
  + Hỗ trợ chụp hình sản phẩm
  + Bàn giao mã nguồn sạch
  - Không bao gồm: Đăng ký Bộ Công Thương

- Gói PREMIUM: 12 - 20 triệu đồng (Cao cấp)
  Trải nghiệm cao cấp và hỗ trợ pháp lý toàn diện
  + Mọi tính năng gói Standard
  + Hỗ trợ làm Website thương mại điện tử
  + Đăng ký Bộ Công Thương
  + SEO nâng cao & Analytics
  + Bảo trì 12 tháng miễn phí
  + Hỗ trợ 24/7
"""

    return f"""
Bạn là nhân viên tư vấn của IPSystem - công ty chuyên phát triển phần mềm.
Hãy tư vấn nhiệt tình, chuyên nghiệp bằng tiếng Việt.
Nếu khách muốn liên hệ, hướng dẫn họ vào trang ipsystem.vn/contact/.

{hero_text}
{service_text}
{portfolio_text}
{pricing_text}

Thông tin liên hệ:
- Trang liên hệ: /contact/
- Nếu không biết câu trả lời, đề nghị khách liên hệ trực tiếp để được tư vấn chi tiết.
"""


@csrf_exempt
def chat(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    try:
        data = json.loads(request.body)
        messages = data.get('messages', [])

        response = groq_client.chat.completions.create(
            model='llama-3.3-70b-versatile',
            messages=[
                {'role': 'system', 'content': get_site_data()},
                *messages
            ],
            max_tokens=1000
        )
        return JsonResponse({'reply': response.choices[0].message.content})

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)