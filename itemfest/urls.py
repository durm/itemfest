from django.conf.urls import include, url
from django.contrib import admin

from itemfest import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'itemfest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^products/', include('products.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
