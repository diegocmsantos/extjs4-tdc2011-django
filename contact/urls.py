from django.conf.urls.defaults import patterns, include, url
from views import *

urlpatterns = patterns('',
    url('view.action/$', view, name='view'),
    url('create.action/$', create, name='create'),
    url('update.action/$', update, name='update'),
    url('delete.action/$', delete, name='delete'),
)