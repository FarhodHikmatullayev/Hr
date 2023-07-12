from django.urls import path
from .views import login_user, register, candidate

app_name = 'accounts'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register, name='sign-up'),
    path('candidate/', candidate, name='candidate'),
]
