from django.urls import path
from .views import SignUp_View
urlpatterns=[
    path('signup/', SignUp_View.as_view(), name='registratsiya'),
]