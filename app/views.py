from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Tokenlarni olish
        tokens = serializer.validated_data
        return Response(tokens, status=status.HTTP_200_OK)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  # Faqat autentifikatsiyalangan foydalanuvchilar uchun

    def get(self, request):
        # Token to'g'ri bo'lsa, bu ma'lumot qaytariladi
        return Response({"message": "Bu himoyalangan yo'lga kirdingiz!"}, status=200)
