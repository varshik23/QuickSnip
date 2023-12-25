from django.urls import path
from .views import redirect_to_long_url, URLShortenView, RegisterApi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# app_name = 'quicksnipserver'
urlpatterns = [
    path('quicksnipserver/Login/', TokenObtainPairView.as_view(), name='Login'),
    path('quicksnipserver/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('quicksnipserver/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('quicksnipserver/register/', RegisterApi.as_view(), name='register'),
    path('quicksnipserver/shorten/', URLShortenView.as_view(), name='url-shorten'),
    path('quicksnipserver/<str:short_url_key>/', redirect_to_long_url, name='redirect-to-long-url'),
]