from django.urls import path
from .views import redirect_url, URLShortenView, RegisterApi, ListUrls, UrlData
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('register/', RegisterApi.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='Login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('shorten/', URLShortenView.as_view(), name='url-shorten'),
    path('myurls/', ListUrls.as_view(), name='get-urls'),
    path('myurls/<int:id>/', UrlData.as_view(), name='get-url-data'),
    path('<str:short_url_key>/', redirect_url, name='redirect-to-long-url'),
]
