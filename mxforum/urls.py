#!/usr/bin/env python3
# vim: fileencoding=utf-8 fdm=indent sw=4 ts=4 sts=4 et
from apps.user import urls as user_urls

urlpatterns = []
urlpatterns += user_urls.urlpatterns
