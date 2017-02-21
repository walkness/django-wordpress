# -*- coding: utf-8 -*-

from django.conf import settings

DATABASE = getattr(settings, "WP_DATABASE", "default")
WP_READ_ONLY = getattr(settings, 'WP_READ_ONLY', True)


class WordpressRouter(object):
    """
    Overrides default wordpress database to WP_DATABASE setting.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'wordpress':
            return DATABASE
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if WP_READ_ONLY:
            return False
        if app_label == 'wordpress':
            return db == 'wordpress'
        return None
