from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import RegisterUserSerializer, LoginUserSerializer


class RegisterUserView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'message': 'user registed successfully'}, status=status.HTTP_201_CREATED)
    

class LoginUserView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        access_token = AccessToken.for_user(user)
        refresh_token = access_token

        return Response({
            'access': str(access_token),
            'refresh':str(refresh_token),
            'username': user.username,
        }, status=status.HTTP_200_OK)


