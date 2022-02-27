from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import DatosUsuarios

class DatosUsuariosSerializer(serializers.ModelSerializer):
    class Meta():
        model = DatosUsuarios
        fields='__all__'

class UsuarioCreateSerializer(serializers.ModelSerializer):
    class Meta():
        model = DatosUsuarios
        fields= ('nombre', 'apellido', 'edad')
class UsuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta():
        model = DatosUsuarios
        fields= ('nombre', 'apellido', 'edad')

