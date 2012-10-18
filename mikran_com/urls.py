from django.conf.urls import patterns, include, url 
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _


from shop import urls as shop_urls # <-- Add this at the top
#from shop.views import ShopTemplateView
from mshop.views import WelcomeListView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mikran_com.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #Home
    url(r'^$', WelcomeListView.as_view()),

                       #(r'^mshop/', include('mshop.urls')),

    #language change
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^country/', include('countries.urls')),
    (r'^currency/', include('currencies.urls')),

    #(r'^shop/', include(shop_urls)),
)

urlpatterns += i18n_patterns('',
    url(_(r'^'), include('mshop.urls')),
    url(r'^shop/', include(shop_urls)),
)
