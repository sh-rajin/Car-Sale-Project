

from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('car_app.urls')),
    path('brands/', include('brands.urls')),
    path('', views.home, name='homepage'),
    path('brand/<slug:brand_slug>/', views.home, name='brand_wise_car'),
    path('buy_now/<int:id>/', views.buy_now, name='buy_now'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
