from django.urls import path
from authentication.views import RegisterUser
# authentication urls

urlpatterns = [
    path('', RegisterUser.as_view(), name='register'),
]