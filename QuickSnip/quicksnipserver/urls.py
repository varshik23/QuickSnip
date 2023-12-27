from django.urls import path
from .views import redirect_to_long_url, URLShortenView, RegisterApi, GetUrls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='Login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterApi.as_view(), name='register'),
    path('shorten/', URLShortenView.as_view(), name='url-shorten'),
    path('myurls/', GetUrls.as_view(), name='get-urls'),
    path('<str:short_url_key>/', redirect_to_long_url, name='redirect-to-long-url'),
]