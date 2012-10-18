# Django settings for mikran_com project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEFAULT_CHARSET = 'utf8'

# In your project's settings.py, add the following line:
#SHOP_PRODUCT_MODEL = 'mshop.models.Product'

ADMINS = (
    ('Tomasz Zdanowski', 'tomasz@mikran.pl'),
)

INTERNAL_IPS = ['127.0.0.1']

MANAGERS = ADMINS

SHOP_CART_MODEL = ('mshop.cart.Cart','shop')

VAT_MODIFIER_CLASS = 'mshop.modifiers.VatPerItemTaxModifier'
CURRENCY_MODIFIER_CLASS = 'mshop.modifiers.CurrencyModifier'
SHOP_CART_MODIFIERS = [VAT_MODIFIER_CLASS, CURRENCY_MODIFIER_CLASS]

gettext = lambda s: s
LANGUAGES = (
    ('fr', gettext(u'French')),
    ('en', gettext('English')),
    ('pl', gettext(u'Polish')),
    ('de', gettext(u'German')),
    ('es', gettext(u'Spanish')),
    ('sk', gettext(u'Sloviakian')),
    )


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    )

HOME_CURRENCY = 'PLN'
DEFAULT_CURRENCY = 'EUR'
CURRENCY_COOKIE_NAME = 'django_currency'
CURRENCIES = (
    ('AED', gettext('United Arab Emirates dirham')),
    ('AFN', gettext('Afghan afghani')),
    ('ALL', gettext('Albanian lek')),
    ('USD', gettext('USD dollar')),
    ('EUR', gettext('Euro')),
    ('PLN', gettext('Pln')),
    ('HUF', gettext('Hungarian forint')),
)

CURRENCIES_LIST = [c[0] for c in CURRENCIES]

"""
http://xml.coverpages.org/country3166.html
Country Code List: ISO 3166-1993 (E)
This international standard provides a two-letter alphabetic code for representing the names of countries, dependencies, and other areas of special geopolitical interest. The source of this code set is the "Codes for the Representation of Names of Countries (ISO 3166-1993 (E))." Note: 2005-04 correction, Nambia --> Namibia.
"""

GEOIP_PATH = '/usr/local/share/GeoIP/'
DEFAULT_COUNTRY = 'PL'
COUNTRY_COOKIE_NAME = 'django_country'
COUNTRIES = (
    ('AD', gettext('Andorra')),
    ('AE', gettext('United Arab Emirates')),
    ('AF', gettext('Afghanistan')),
    ('AG', gettext('Antigua & Barbuda')),
    ('AI', gettext('Anguilla')),
    ('AL', gettext('Albania')),
    ('AM', gettext('Armenia')),
    ('AN', gettext('Netherlands Antilles')),
    ('AO', gettext('Angola')),
    ('AQ', gettext('Antarctica')),
    ('AR', gettext('Argentina')),
    ('AS', gettext('American Samoa')),
    ('AT', gettext('Austria')),
    ('AU', gettext('Australia')),
    ('AW', gettext('Aruba')),
    ('AZ', gettext('Azerbaijan')),
    ('BA', gettext('Bosnia and Herzegovina')),
    ('BB', gettext('Barbados')),
    ('BD', gettext('Bangladesh')),
    ('BE', gettext('Belgium')),
    ('BF', gettext('Burkina Faso')),
    ('BG', gettext('Bulgaria')),
    ('BH', gettext('Bahrain')),
    ('BI', gettext('Burundi')),
    ('BJ', gettext('Benin')),
    ('BM', gettext('Bermuda')),
    ('BN', gettext('Brunei Darussalam')),
    ('BO', gettext('Bolivia')),
    ('BR', gettext('Brazil')),
    ('BS', gettext('Bahama')),
    ('BT', gettext('Bhutan')),
    ('BV', gettext('Bouvet Island')),
    ('BW', gettext('Botswana')),
    ('BY', gettext('Belarus')),
    ('BZ', gettext('Belize')),
    ('CA', gettext('Canada')),
    ('CC', gettext('Cocos (Keeling) Islands')),
    ('CF', gettext('Central African Republic')),
    ('CG', gettext('Congo')),
    ('CH', gettext('Switzerland')),
    ('CI', gettext('Ivory Coast')),
    ('CK', gettext('Cook Iislands')),
    ('CL', gettext('Chile')),
    ('CM', gettext('Cameroon')),
    ('CN', gettext('China')),
    ('CO', gettext('Colombia')),
    ('CR', gettext('Costa Rica')),
    ('CU', gettext('Cuba')),
    ('CV', gettext('Cape Verde')),
    ('CX', gettext('Christmas Island')),
    ('CY', gettext('Cyprus')),
    ('CZ', gettext('Czech Republic')),
    ('DE', gettext('Germany')),
    ('DJ', gettext('Djibouti')),
    ('DK', gettext('Denmark')),
    ('DM', gettext('Dominica')),
    ('DO', gettext('Dominican Republic')),
    ('DZ', gettext('Algeria')),
    ('EC', gettext('Ecuador')),
    ('EE', gettext('Estonia')),
    ('EG', gettext('Egypt')),
    ('EH', gettext('Western Sahara')),
    ('ER', gettext('Eritrea')),
    ('ES', gettext('Spain')),
    ('ET', gettext('Ethiopia')),
    ('FI', gettext('Finland')),
    ('FJ', gettext('Fiji')),
    ('FK', gettext('Falkland Islands (Malvinas)')),
    ('FM', gettext('Micronesia')),
    ('FO', gettext('Faroe Islands')),
    ('FR', gettext('France')),
    ('FX', gettext('France, Metropolitan')),
    ('GA', gettext('Gabon')),
    ('GB', gettext('United Kingdom (Great Britain)')),
    ('GD', gettext('Grenada')),
    ('GE', gettext('Georgia')),
    ('GF', gettext('French Guiana')),
    ('GH', gettext('Ghana')),
    ('GI', gettext('Gibraltar')),
    ('GL', gettext('Greenland')),
    ('GM', gettext('Gambia')),
    ('GN', gettext('Guinea')),
    ('GP', gettext('Guadeloupe')),
    ('GQ', gettext('Equatorial Guinea')),
    ('GR', gettext('Greece')),
    ('GS', gettext('South Georgia and the South Sandwich Islands')),
    ('GT', gettext('Guatemala')),
    ('GU', gettext('Guam')),
    ('GW', gettext('Guinea-Bissau')),
    ('GY', gettext('Guyana')),
    ('HK', gettext('Hong Kong')),
    ('HM', gettext('Heard & McDonald Islands')),
    ('HN', gettext('Honduras')),
    ('HR', gettext('Croatia')),
    ('HT', gettext('Haiti')),
    ('HU', gettext('Hungary')),
    ('ID', gettext('Indonesia')),
    ('IE', gettext('Ireland')),
    ('IL', gettext('Israel')),
    ('IN', gettext('India')),
    ('IO', gettext('British Indian Ocean Territory')),
    ('IQ', gettext('Iraq')),
    ('IR', gettext('Islamic Republic of Iran')),
    ('IS', gettext('Iceland')),
    ('IT', gettext('Italy')),
    ('JM', gettext('Jamaica')),
    ('JO', gettext('Jordan')),
    ('JP', gettext('Japan')),
    ('KE', gettext('Kenya')),
    ('KG', gettext('Kyrgyzstan')),
    ('KH', gettext('Cambodia')),
    ('KI', gettext('Kiribati')),
    ('KM', gettext('Comoros')),
    ('KN', gettext('St. Kitts and Nevis')),
    ('KP', gettext('Korea, Democratic People\'s Republic of')),
    ('KR', gettext('Korea, Republic of')),
    ('KW', gettext('Kuwait')),
    ('KY', gettext('Cayman Islands')),
    ('KZ', gettext('Kazakhstan')),
    ('LA', gettext('Lao People\'s Democratic Republic')),
    ('LB', gettext('Lebanon')),
    ('LC', gettext('Saint Lucia')),
    ('LI', gettext('Liechtenstein')),
    ('LK', gettext('Sri Lanka')),
    ('LR', gettext('Liberia')),
    ('LS', gettext('Lesotho')),
    ('LT', gettext('Lithuania')),
    ('LU', gettext('Luxembourg')),
    ('LV', gettext('Latvia')),
    ('LY', gettext('Libyan Arab Jamahiriya')),
    ('MA', gettext('Morocco')),
    ('MC', gettext('Monaco')),
    ('MD', gettext('Moldova, Republic of')),
    ('MG', gettext('Madagascar')),
    ('MH', gettext('Marshall Islands')),
    ('ML', gettext('Mali')),
    ('MN', gettext('Mongolia')),
    ('MM', gettext('Myanmar')),
    ('MO', gettext('Macau')),
    ('MP', gettext('Northern Mariana Islands')),
    ('MQ', gettext('Martinique')),
    ('MR', gettext('Mauritania')),
    ('MS', gettext('Monserrat')),
    ('MT', gettext('Malta')),
    ('MU', gettext('Mauritius')),
    ('MV', gettext('Maldives')),
    ('MW', gettext('Malawi')),
    ('MX', gettext('Mexico')),
    ('MY', gettext('Malaysia')),
    ('MZ', gettext('Mozambique')),
    ('NA', gettext('Namibia')),
    ('NC', gettext('New Caledonia')),
    ('NE', gettext('Niger')),
    ('NF', gettext('Norfolk Island')),
    ('NG', gettext('Nigeria')),
    ('NI', gettext('Nicaragua')),
    ('NL', gettext('Netherlands')),
    ('NO', gettext('Norway')),
    ('NP', gettext('Nepal')),
    ('NR', gettext('Nauru')),
    ('NU', gettext('Niue')),
    ('NZ', gettext('New Zealand')),
    ('OM', gettext('Oman')),
    ('PA', gettext('Panama')),
    ('PE', gettext('Peru')),
    ('PF', gettext('French Polynesia')),
    ('PG', gettext('Papua New Guinea')),
    ('PH', gettext('Philippines')),
    ('PK', gettext('Pakistan')),
    ('PL', gettext('Poland')),
    ('PM', gettext('St. Pierre & Miquelon')),
    ('PN', gettext('Pitcairn')),
    ('PR', gettext('Puerto Rico')),
    ('PT', gettext('Portugal')),
    ('PW', gettext('Palau')),
    ('PY', gettext('Paraguay')),
    ('QA', gettext('Qatar')),
    ('RE', gettext('Reunion')),
    ('RO', gettext('Romania')),
    ('RU', gettext('Russian Federation')),
    ('RW', gettext('Rwanda')),
    ('SA', gettext('Saudi Arabia')),
    ('SB', gettext('Solomon Islands')),
    ('SC', gettext('Seychelles')),
    ('SD', gettext('Sudan')),
    ('SE', gettext('Sweden')),
    ('SG', gettext('Singapore')),
    ('SH', gettext('St. Helena')),
    ('SI', gettext('Slovenia')),
    ('SJ', gettext('Svalbard & Jan Mayen Islands')),
    ('SK', gettext('Slovakia')),
    ('SL', gettext('Sierra Leone')),
    ('SM', gettext('San Marino')),
    ('SN', gettext('Senegal')),
    ('SO', gettext('Somalia')),
    ('SR', gettext('Suriname')),
    ('ST', gettext('Sao Tome & Principe')),
    ('SV', gettext('El Salvador')),
    ('SY', gettext('Syrian Arab Republic')),
    ('SZ', gettext('Swaziland')),
    ('TC', gettext('Turks & Caicos Islands')),
    ('TD', gettext('Chad')),
    ('TF', gettext('French Southern Territories')),
    ('TG', gettext('Togo')),
    ('TH', gettext('Thailand')),
    ('TJ', gettext('Tajikistan')),
    ('TK', gettext('Tokelau')),
    ('TM', gettext('Turkmenistan')),
    ('TN', gettext('Tunisia')),
    ('TO', gettext('Tonga')),
    ('TP', gettext('East Timor')),
    ('TR', gettext('Turkey')),
    ('TT', gettext('Trinidad & Tobago')),
    ('TV', gettext('Tuvalu')),
    ('TW', gettext('Taiwan, Province of China')),
    ('TZ', gettext('Tanzania, United Republic of')),
    ('UA', gettext('Ukraine')),
    ('UG', gettext('Uganda')),
    ('UM', gettext('United States Minor Outlying Islands')),
    ('US', gettext('United States of America')),
    ('UY', gettext('Uruguay')),
    ('UZ', gettext('Uzbekistan')),
    ('VA', gettext('Vatican City State (Holy See)')),
    ('VC', gettext('St. Vincent & the Grenadines')),
    ('VE', gettext('Venezuela')),
    ('VG', gettext('British Virgin Islands')),
    ('VI', gettext('United States Virgin Islands')),
    ('VN', gettext('Viet Nam')),
    ('VU', gettext('Vanuatu')),
    ('WF', gettext('Wallis & Futuna Islands')),
    ('WS', gettext('Samoa')),
    ('YE', gettext('Yemen')),
    ('YT', gettext('Mayotte')),
    ('YU', gettext('Yugoslavia')),
    ('ZA', gettext('South Africa')),
    ('ZM', gettext('Zambia')),
    ('ZR', gettext('Zaire')),
    ('ZW', gettext('Zimbabwe')),
    ('ZZ', gettext('Unknown or unspecified country')),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mshop',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'zdanek123',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3305',                      # Set to empty string for default. Not used with sqlite3.
    },
    'legacy_mikran': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mikran_1',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'zdanek123',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3305',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Warsaw'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    '/home/tomasz/workspace/mikran_com/static',
    '/home/tomasz/project/mikran_com/static',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'biu%e&amp;xcrs9f@8v)u6pvx1h!r1b#nb*!$0xx3!1!ck5e3945d!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

##############
# MIDDLEWARE #
##############

# List of middleware classes to use.  Order is important; in the request phase,
# this middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'currencies.middleware.CurrencyLocaleMiddleware',
    'countries.middleware.CountryLocaleMiddleware',
    #'mshop.middleware.VatLocaleMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS':False,
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
)

ROOT_URLCONF = 'mikran_com.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mikran_com.wsgi.application'

import os
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    PROJECT_PATH + '/../',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'polymorphic',
    'south',
    'shop',
    'shop.addressmodel',
    'mshop',
    'countries',
    'currencies',
    'legacy',
    'curr_conv',
    'debug_toolbar',
    #'multilingual',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
