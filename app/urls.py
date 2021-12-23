
from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import MyTokenObtainPairView , getNotes , login , profile , cookies , getcookies

urlpatterns = [

    path('api/token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('notes', getNotes),
    path('login/', login),
    path('profile/', profile),
    path('cookies', cookies),
    path('getcookies', getcookies),

] 