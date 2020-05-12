"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include, url
from pizzapi.views import UserAPIView, RegisterAPIView, LoginAPIView, PizzaViewSet, OrderViewSet
from rest_framework import routers
from knox.views import LogoutView
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.generic.base import RedirectView


schema_view = get_schema_view(
   openapi.Info(
      title="Yummy Pizza API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="adetulatolu@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



router = routers.DefaultRouter()
router.register(r'pizzas', PizzaViewSet)
router.register(r'orders', OrderViewSet)



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('auth', include('knox.urls')),
    path('auth/user', UserAPIView.as_view()),
    path('auth/register', RegisterAPIView.as_view()),
    path('auth/login', LoginAPIView.as_view()),
    path('auth/logout', LogoutView.as_view(), name='knox_logout'),
    path('api/', include(router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('api/swagger/doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/redoc/doc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('', RedirectView.as_view(url='api/swagger/doc', permanent=False),)
]
