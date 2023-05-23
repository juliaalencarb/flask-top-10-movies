from application.model import init_model


class DatabaseService:
    instance = None

    def init_app(self, instance):
        self.instance = instance
        init_model(instance)


database_service = DatabaseService()
