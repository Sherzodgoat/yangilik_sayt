from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView,
                                       PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import path

from account.views import ProfileView, EditProfileView, logout_request_view, user_profile_view, SignupView

urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout-req/', logout_request_view, name = 'logout_req'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('profile/', user_profile_view, name = 'profile'),
    path('profile-edit/', EditProfileView.as_view(), name = 'profile_edit'),

    path('register/', SignupView.as_view(), name='register'),

    # password change

    path('password_change/', PasswordChangeView.as_view(), name = 'password_change'),
    path('profile/password/change-done/', PasswordChangeDoneView.as_view(), name = 'password_change_done'),

    # password resed
    path('password-reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
