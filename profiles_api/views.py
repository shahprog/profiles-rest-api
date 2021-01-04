from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return  a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as a function (get, post, put, patch, delete)',
            'Is simlar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to application logic'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle upadting an object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, requst, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            "Uses action (list, create, retrieve, update, partial_update)",
            "Automatically maps to URLs using routers",
            "Provides more functionality with less code"
        ]

        return Response({
            'message': "hello",
            'a_viewset': a_viewset
        })
    
    def create(self, request):
        """Post method"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message': name})
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """GET method"""

        return Response({'method': 'GET'})


    def update(self, request, pk=None):
        """PUT method"""

        return Response({'method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """PUT method"""

        return Response({'method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """PUT method"""

        return Response({'method': 'DELETE'})