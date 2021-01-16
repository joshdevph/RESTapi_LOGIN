from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apis.login_api.urls')),
    path('api/register/', include('apis.register_api.urls')),
    path('login_view/', include('apps.login_app.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
