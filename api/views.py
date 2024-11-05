from rest_framework import viewsets, generics, authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from .serializer import ProductoSerializer, ProductoSerializer,  AuthTokenSerializer , UserSerializer
from .models import Productos

class UsurioViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = UserSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializer

class CreateProductoView(generics.CreateAPIView):
    serializer_class = ProductoSerializer

class RetreiIveUpdateProdictoView(generics.RetrieveUpdateAPIView):
    serializer_class = ProductoSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        queryset = Productos.objects.all()
        serializer_class = ProductoSerializer
        return self.request.ProductoViewSet


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer