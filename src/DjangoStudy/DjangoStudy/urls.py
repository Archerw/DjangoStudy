from django.conf.urls import patterns, include, url
from DjangoStudy.views import hello

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',('^hello/$',hello),
    # Examples:
    # url(r'^$', 'DjangoStudy.views.home', name='home'),
    # url(r'^DjangoStudy/', include('DjangoStudy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
