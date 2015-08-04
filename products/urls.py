from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^product/(?P<product_id>[0-9]+)/$', views.product_view, name='product_view'),
]