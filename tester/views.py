from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView


class Index(APIView):
  def get(self, request, *args, **kwargs):
    return Response({'message': 'success'}, status=HTTP_200_OK)
