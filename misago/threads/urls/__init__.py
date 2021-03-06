from django.conf import settings
from django.conf.urls import patterns, url

from misago.threads.views.threadslist import (
    ThreadsList, CategoryThreadsList, PrivateThreadsList)


PATTERNS_KWARGS = (
    {'list_type': 'all'},
    {'list_type': 'my'},
    {'list_type': 'new'},
    {'list_type': 'unread'},
    {'list_type': 'subscribed'},
    {'list_type': 'unapproved'},
)


def threads_list_patterns(root_name, view, patterns):
    urlpatterns = []

    for i, pattern in enumerate(patterns):
        if i > 0:
            url_name = '%s-%s' % (root_name, PATTERNS_KWARGS[i]['list_type'])
        else:
            url_name = root_name

        urlpatterns.append(url(
            pattern,
            view.as_view(),
            name=url_name,
            kwargs=PATTERNS_KWARGS[i],
        ))

    return urlpatterns


if settings.MISAGO_CATEGORIES_ON_INDEX:
    urlpatterns = threads_list_patterns('threads', ThreadsList, (
        r'^threads/$',
        r'^threads/my/$',
        r'^threads/new/$',
        r'^threads/unread/$',
        r'^threads/subscribed/$',
        r'^threads/unapproved/$',
    ))
else:
    urlpatterns = threads_list_patterns('threads', ThreadsList, (
        r'^$',
        r'^my/$',
        r'^new/$',
        r'^unread/$',
        r'^subscribed/$',
        r'^unapproved/$',
    ))


urlpatterns += threads_list_patterns('category', CategoryThreadsList, (
    r'^category/(?P<slug>[-a-zA-Z0-9]+)-(?P<pk>\d+)/$',
    r'^category/(?P<slug>[-a-zA-Z0-9]+)-(?P<pk>\d+)/my/$',
    r'^category/(?P<slug>[-a-zA-Z0-9]+)-(?P<pk>\d+)/new/$',
    r'^category/(?P<slug>[-a-zA-Z0-9]+)-(?P<pk>\d+)/unread/$',
    r'^category/(?P<slug>[-a-zA-Z0-9]+)-(?P<pk>\d+)/subscribed/$',
    r'^category/(?P<slug>[-a-zA-Z0-9]+)-(?P<pk>\d+)/unapproved/$',
))


urlpatterns += threads_list_patterns('private-threads', CategoryThreadsList, (
    r'^private-threads/$',
    r'^private-threads/my/$',
    r'^private-threads/new/$',
    r'^private-threads/unread/$',
    r'^private-threads/subscribed/$',
    r'^private-threads/unapproved/$',
))