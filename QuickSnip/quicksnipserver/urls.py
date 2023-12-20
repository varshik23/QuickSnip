from django.urls import path
from .views import redirect_to_long_url, URLShortenView

app_name = 'quicksnipserver'
urlpatterns = [
    path('quicksnipserver:shorten/', URLShortenView.as_view(), name='url-shorten'),
    path('quicksnipserver:<str:short_url_key>/', redirect_to_long_url, name='redirect-to-long-url'),
]