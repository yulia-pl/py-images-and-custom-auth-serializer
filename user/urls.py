from django.urls import path
from .views import CreateUserView, CustomAuthToken, ManageUserView

app_name = "user"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CustomAuthToken.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),
]
