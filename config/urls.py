from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Mobile app API system",
        default_version='v1',
        description="The Mobile App API System is a comprehensive set of web services designed to facilitate \n "
                    "communication between a mobile application and a server. It enables the app to send and receive \n"
                    "data, perform operations, and interact with various functionalities of the server-side system. \n",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="inomjonqurbonov916@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # my apps
    path('ielts/', include('ielts_test.urls'))
]
