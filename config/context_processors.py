from .models import Configuration


def settings(request):
    return {'settings': Configuration.load()}
