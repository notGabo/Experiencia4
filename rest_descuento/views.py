from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from CommunityPlant.models import Descuento
from .serializers import DescuentoSerializer
@csrf_exempt
@api_view(['GET','POST'])
# Create your views here.
def lista_descuento(request):
    """
    lista de los descuento
    """
    if request.method == 'GET':
        descuento = Descuento.objects.all()
        serializer = DescuentoSerializer(descuento,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        print("entre 1")
        #data = JSONParser().parse(request)
        serializer = DescuentoSerializer(data = request.data)
        if serializer.is_valid():
            print("entre al valido")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def detalle_descuento (request,id):
    """
    get, update o delete de un descuento
    """
    try: descuento = Descuento.objects.get(IdCodigo=id)
    except Descuento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DescuentoSerializer(descuento)
        return Response(serializer.data)
    if request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = DescuentoSerializer(descuento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        descuento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
