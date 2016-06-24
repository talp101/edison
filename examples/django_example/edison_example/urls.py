from django.conf.urls import url
from .views import AuthUsersView

urlpatterns = [
    url(r'^auth_users/', AuthUsersView.as_view())
]
