#ref:https://www.django-rest-framework.org/api-guide/renderers/
#example ref:https://github.com/encode/django-rest-framework/blob/master/tests/test_htmlrenderer.py

from email import charset
from rest_framework.renderers import TemplateHTMLRenderer # we use this inside the child  class
from rest_framework.response import Response # we will use inside the method for creating queryset
from rest_framework import generics#we inherit this class
from App.models import Identity
from rest_framework.views import APIView

class Child(APIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name='App/index.html'
    media_type="text/html"
    charset='utf-8'

    def get(self, request, *args, **kwargs):
        queryset = Identity.objects.all()
        return Response({'user': queryset})
#ref:https://stackoverflow.com/questions/63086353/django-self-renderer-classes-object-of-type-type-has-no-len