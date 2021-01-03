from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Return  a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as a function (get, post, put, patch, delete)',
            'Is simlar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to application logic'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})