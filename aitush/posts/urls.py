from django.conf.urls import url
# from django.contrib import admin
from .views import (
    index,
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    )


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^blog/$', post_list, name="list"),
    url(r'^blog/create/$', post_create, name="create"),
    url(r'^blog/(?P<slug>[\w-]+)/$', post_detail, name="detail"),
    url(r'^blog/(?P<slug>[\w-]+)/edit/$', post_update, name="update"),
    url(r'^blog/(?P<slug>[\w-]+)/delete/$', post_delete, name="delete"),
    # url(r'^posts/$', "<appname>.views.<function_name>"),
    ]
