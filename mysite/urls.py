from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import loginx
from login.views import addx
from login.views import TESTAPI_resetFixturex
from login.views import TESTAPI_unitTests

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),rs
    #url(r'^users/login', loginx),
    #url(r'^users/add', addx),
    #url(r'^TESTAPI/resetFixture', TESTAPI_resetFixturex),
    url(r'^users/login', loginx),
    url(r'^users/add', addx),
    url(r'^TESTAPI/resetFixture', TESTAPI_resetFixturex),
    url(r'^TESTAPI/unitTests', TESTAPI_unitTests) 
)
