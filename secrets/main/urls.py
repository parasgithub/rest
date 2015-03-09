from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
import main.views as views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'secrets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^$', views.api_root),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    url(r'^secrets/$', views.SecretListCreate.as_view(), name='secret-list'),
    url(r'^secrets/(?P<pk>[0-9]+)/$', views.SecretDetail.as_view(), name='secret-detail'),
)
