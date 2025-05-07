from django.shortcuts import render
from professionals.serializers import ProfessionalSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Professionals


@api_view(['GET'])
def list_professional(request):
    if request.method == 'GET':
        professional = Professionals.objects.all()
        print(f'dados:{professional}')
        serializer = ProfessionalSerializer(professional, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def register_professional(request):
    if request.method == 'POST':
        serializer = ProfessionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'PATCH'])
def detail_professional(request, pk):
    try:
        professional = Professionals.objects.get(pk=pk)
    except Professionals.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    partial = request.method == 'PATCH'
    serializer = ProfessionalSerializer(professional, data=request.data, partial=partial)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_professional(request, pk):
    
    try:
        professional = Professionals.objects.get(pk=pk)
    except Professionals.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    professional.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)