from django.urls import path
from .views import MyTokenObtainPairView,ProtectedView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('some_protected_route/', ProtectedView.as_view(), name='protected'),  # Himoyalangan route
]
