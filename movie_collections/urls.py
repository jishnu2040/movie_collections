
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')), 
    path('api/v1/core/', include('api.urls')),
    path('api/v1/accounts/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/accounts/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
