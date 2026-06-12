from django.apps import AppConfig


class ClangConfig(AppConfig):
    name = 'conlangapp'

    def ready(self):
        import conlangapp.signals