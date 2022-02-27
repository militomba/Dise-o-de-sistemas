#from django.shortcuts import get_object_or_404
from functools import partial
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from .models import DatosUsuarios
from .serializers import (DatosUsuariosSerializer, UsuarioCreateSerializer, UsuarioUpdateSerializer)
class UsuariosViewSets(viewsets.ViewSet):
    
    def UserList(self,request):
        user= DatosUsuarios.objects.all()
        serializer = DatosUsuariosSerializer(user, many=True)
        return Response(serializer.data)

    
    def CreateUser(self,request):
        post_data = request.data
        serializer = UsuarioCreateSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    
    def UpdateUser(self,request, pk=None):
        post_data = request.data
        user = DatosUsuarios.objects.get(pk=pk)
        serializer = UsuarioUpdateSerializer(user, data=post_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    
    def DeleteUser(self,request, pk=None):
        user = DatosUsuarios.objects.get(pk=pk)
        user.delete()
        return Response("Usuario Eliminado")
        
