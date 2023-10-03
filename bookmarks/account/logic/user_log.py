# logic/user_log.py

from django.contrib.auth import authenticate, login
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


from account.forms import LoginForm


def _log_in(request: WSGIRequest) -> HttpResponse | None:
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )

            if user is not None and user.is_active:
                login(request, user)

                # можно ридерект на успешную страницу
                return HttpResponse('successfull')

            return HttpResponse('ivalid login')
        return form
