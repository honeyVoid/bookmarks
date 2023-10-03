from django.urls import path
from django.contrib.auth import views as av

from . import views


urlpatterns = [
    path('login/', av.LoginView.as_view(), name='login'),
    path('logout/', av.LogoutView.as_view(), name='logout'),


    path('', views.dashboard, name='dashboard'),


    path(
        'password-change/',
        av.PasswordChangeView.as_view(),
        name='password_change'
    ),
    path(
        'password-change/done/',
        av.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),


    path(
        'password_reset/',
        av.PasswordResetView.as_view(),
        name='password_reset'
    ),

    path(
        'password-reset/done/',
        av.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'password-reset/<uidb64>/<token>/',
        av.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'password-reset/complete/',
        av.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    )
]

