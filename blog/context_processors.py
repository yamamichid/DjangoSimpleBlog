from .models import BlogConfig


def blog_config(request):
    return {'blog_config': BlogConfig.load()}
