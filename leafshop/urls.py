from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog
from django.views.generic import RedirectView


urlpatterns = [
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('shop.urls'), name='shop'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('favicon.ico/', RedirectView.as_view(url='/static/media/favicon.ico')),
    prefix_default_language=False
)

admin.site.site_header = "LeafShop Admin"
admin.site.site_title = "LeafShop Admin"
admin.site.index_title = "Welcome to LeafShop admin panel"
