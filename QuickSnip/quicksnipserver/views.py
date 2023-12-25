from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import urls
from .serializers import urlsSerializer, RegisterSerializer, UserSerializer

# Create your views here.
#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

class URLShortenView(generics.ListCreateAPIView):
    serializer_class = urlsSerializer

    def create(self, request, *args, **kwargs):
        long_url = request.data.get('url')
        print(request)
        alias = ''
        if request.data.get('alias'):
            alias = request.data.get('alias')
        if long_url:
            # Generate a short URL key (you can use a more advanced method)
            short_url_key = "" if not alias else alias
            url_data = {'url': long_url, 'short_url': short_url_key}
            serializer = self.get_serializer(data=url_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        else:
            return Response({'error': 'Missing "long_url" in the request'}, status=400)

@api_view(['GET'])
def redirect_to_long_url(request, short_url_key):
    url = get_object_or_404(urls, short_url=short_url_key)
    return redirect(url.url)
