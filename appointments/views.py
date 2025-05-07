from appointments.serializers import AppointmentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Appointment
from professionals.models import Professionals

@api_view(['GET'])
def list_appointments(request):
    professional_id = request.query_params.get('professional_id')
    
    if professional_id:
        try:
            professional = Professionals.objects.get(pk=professional_id)
        except Professionals.DoesNotExist:
            return Response({'detail': 'Professional not found'}, status=status.HTTP_404_NOT_FOUND)
        
        appointments = Appointment.objects.filter(professional=professional)
    else:
        appointments = Appointment.objects.all()
        
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def register_appointment(request):
    if request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def detail_appointment(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    partial = request.method == 'PACTH'
    serializer = AppointmentSerializer(appointment, data=request.data, partial=partial)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_appointment(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    appointment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
