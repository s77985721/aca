from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Productos
from .models import Usuarios

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuarios
        fields= ('Id_Usuario','Username','email','Password')
        read_only_field= ('Id_Usuario')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_Producto_model()
# #         fields = ['id','nombre','categoria','descripcion', 'ṕrecio','stock']
# #         extr_kwargs = {'password': {'write_only': True}} 

# #     def create(self, validate_data):
# #         return get_Productos_model().create_Producto(**validate_data)

# #     def update(self, instance, validated_data):
# #         password = validated_data.pop('password', None)
# #         Producto = super().update(instance, Validate_data)

# #         if password:
# #             Producto.set_password(password)
# #             Producto.save()

#         return Producto
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if not Productos:
            raise serializers.ValidattionError('No se pudo autenticar', code='authorization')
        data['producto'] = Productos
        return data