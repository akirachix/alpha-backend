
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Users
class UserLocation(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=400)
        try:
            user = Users.objects.get(email=email)
            return Response({
                'full_name': user.full_name,
                'latitude': user.latitude,
                'longitude': user.longitude
            }, status=200)
        except Users.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
    def post(self, request):
        data = request.data
        required_fields = ['full_name', 'email', 'phone_number', 'password', 'latitude', 'longitude', 'user_type']
        if not all(field in data for field in required_fields):
            return Response({'error': 'Missing fields in request'}, status=400)
        if Users.objects.filter(email=data['email']).exists():
            return Response({'error': 'User already exists'}, status=400)
        Users.objects.create(**data)
        return Response({'message': 'User created successfully'}, status=201)
    def put(self, request):
        data = request.data
        email = data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=400)
        try:
            user = Users.objects.get(email=email)
            user.latitude = data.get('latitude', user.latitude)
            user.longitude = data.get('longitude', user.longitude)
            user.save()
            return Response({'message': 'Location updated successfully'}, status=200)
        except Users.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
    def delete(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=400)
        try:
            user = Users.objects.get(email=email)
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=204)
        except Users.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)