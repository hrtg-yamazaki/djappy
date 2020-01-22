from django.conf import settings

def check_debug(request):
    return { "DEBUG": settings.DEBUG }