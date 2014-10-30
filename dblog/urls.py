from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.blog_list', name='blog_list'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/guoc/project/dblog/static'}),
)
