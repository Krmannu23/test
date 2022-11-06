
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view 
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('App.urls')),
    path('admin/', admin.site.urls),#password:123mannu username:mannu
    path('openapi', get_schema_view(
        title="Service",
        description="API development"
    ), name='openapi-schema'),
     path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

]
