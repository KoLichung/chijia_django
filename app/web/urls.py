from django.contrib.sitemaps.views import sitemap
from django.urls import path

from .sitemaps import StaticViewSitemap
from . import views

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('privacy_policy_others', views.privacy_policy_others, name='privacy_policy_others'),
    path('', views.index, name='index'),
    path('price', views.price, name='price'),
    path('works', views.works, name='works'),
    path('contact', views.contact, name='contact'),
    path('message_sent', views.message_sent, name='message_sent'),
    path('app/suppervisionbuy_support', views.suppervisionbuy_support),

    path('sitemap.xml', sitemap, 
            {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap'
        ),
]