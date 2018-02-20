class SimpleDatabaseRouter:
    """
    A router to control all database operations
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read
        """
        if model._meta.app_label == 'mp_rest_api':
            return 'mp'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write
        """
        if model._meta.app_label == 'mp_rest_api':
            return 'mp'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model is involved.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure difference app only storage in specific database.
        """
        if app_label == 'mp_rest_api':
            return db == 'mp'
        return None