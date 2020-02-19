from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class Pyhome(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main.html'

    def get(self,request):
        return Response({}, status=status.HTTP_200_OK)