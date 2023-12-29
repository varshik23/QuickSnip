import hashlib

from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from django.utils.decorators import method_decorator

from .models import urls, clicks
from .serializers import urlsSerializer, RegisterSerializer, UserSerializer, clicksSerializer

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

@permission_classes([IsAuthenticated])
class URLShortenView(generics.ListCreateAPIView):
    http_method_names = ['post']   
    serializer_class = urlsSerializer
    def create(self, request, *args, **kwargs):
        long_url = request.data.get('url')
        alias = ''
        if request.data.get('alias'):
            alias = request.data.get('alias')
        if long_url:
            short_url_key = hashlib.shake_256(long_url.encode()).hexdigest(5) if not alias else alias
            url_data = {'url': long_url, 'short_url': short_url_key, 'user': request.user.pk}
            serializer = self.get_serializer(data=url_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        else:
            return Response({'error': 'Missing "long_url" in the request'}, status=400)

@permission_classes([IsAuthenticated])
class ListUrls(generics.ListCreateAPIView):
    http_method_names = ['get']
    serializer_class = urlsSerializer
    @swagger_auto_schema(query_serializer=urlsSerializer)
    def get_queryset(self):
        return urls.objects.filter(user=self.request.user.pk)

@permission_classes([IsAuthenticated])
class GetUrlData(generics.RetrieveAPIView):
    serializer_class = urlsSerializer
    lookup_field = 'id'
    def get_queryset(self, *args, **kwargs):
        return urls.objects.filter(id=self.kwargs['id'])

@api_view(['GET'])
@permission_classes([])
def redirect_url(request, short_url_key):
    url = get_object_or_404(urls, short_url=short_url_key)
    if clicks.objects.filter(url=url.pk).exists():
        click = clicks.objects.get(url=url.pk)
        click.number_of_clicks += 1
        click.save()
    else:
        serializer = clicksSerializer(data={'url': url.pk, 'number_of_clicks': 1})
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
    return redirect(url.url)
