from django.core.exceptions import PermissionDenied

def login_required(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request, *args, **kwargs)
        return PermissionDenied

    wrapper.__doc__ = function.__doc__
    wrapper.__name__ = function.__name__
    return wrapper
