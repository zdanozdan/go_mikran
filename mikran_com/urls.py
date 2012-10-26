from django.conf.urls import patterns, include, url 
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from django.views.generic.simple import direct_to_template


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

    #language change
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^country/', include('countries.urls')),
    (r'^currency/', include('currencies.urls')),
)

urlpatterns += patterns('',
   (r'^accounts/register/$', 'registration.views.register', { 'template_name': 'auth/registration_form.html', 'backend':'mshop.backend.MikranBackend' }),
   (r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'auth/password_reset_form.html'}),
   (r'^accounts/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name': 'auth/password_reset_confirm.html' }),
   (r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'auth/password_reset_done.html'}),
   (r'^accounts/password/reset/complete/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'auth/password_reset_complete.html'}),
   (r'^accounts/password/change/$', 'django.contrib.auth.views.password_change', {'template_name': 'auth/password_change_form.html'}),
   (r'^accounts/password/change/done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'auth/password_change_done.html'}),
   (r'^accounts/', include('registration.backends.default.urls')),
)

urlpatterns += i18n_patterns('',
    url(_(r'^'), include('mshop.urls')),
    url(r'^shop/', include(shop_urls)),
)
