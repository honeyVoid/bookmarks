# views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .logic.user_log import _log_in


def user_login(request):
    result = _log_in(request)
    if isinstance(result, HttpResponse):
        return result
    return render(
        request,
        'account/login.html',
        {'form': result}
    )


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {
        'selection': 'dashboard'
    })
