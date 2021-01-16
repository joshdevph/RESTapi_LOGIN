from django.urls import path
from .views import LoginApiView, LogoutAPI

urlpatterns = [
    path("login/", LoginApiView.as_view(), name="login-api"),
    path("logout/", LogoutAPI.as_view(), name="logout-api")
]
