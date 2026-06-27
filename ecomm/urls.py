from django.contrib import admin
from django.urls import path
from .views import index,about, contact, blog_list, product, testimonial
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="home"),
    path("/about", about, name="about"),
    path("/contact", contact, name="contact"),
    path("/blog", blog_list, name="blog_list"),
    path("/product", product, name="product"),
    path("/testimonial", testimonial, name="testimonial"),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)