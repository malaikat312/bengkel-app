from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bengkel, Layanan
from .serializers import BengkelSerializer, LayananSerializer, UserSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.http import Http404
from django.contrib.auth.models import User 


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                # Ambil informasi tambahan dari user yang berhasil login
                user_data = {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                }
                # Mengembalikan token dan data pengguna dalam respons
                return Response({'token': token.key, 'user': user_data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BengkelListCreateAPIView(APIView):
    def get(self, request):
        bengkels = Bengkel.objects.all()
        serializer = BengkelSerializer(bengkels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BengkelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class BengkelRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Bengkel.objects.get(pk=pk)
        except Bengkel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        bengkel = self.get_object(pk)
        serializer = BengkelSerializer(bengkel)
        return Response(serializer.data)

    def put(self, request, pk):
        bengkel = self.get_object(pk)
        serializer = BengkelSerializer(bengkel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        bengkel = self.get_object(pk)
        bengkel.delete()
        return Response(status=204)

class LayananListCreateAPIView(generics.ListCreateAPIView):
    queryset = Layanan.objects.all()
    serializer_class = LayananSerializer

class LayananRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Layanan.objects.all()
    serializer_class = LayananSerializer
