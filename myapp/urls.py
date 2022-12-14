# djsr/authentication/urls.py
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView, SaveSchedule, PatchSchedule

urlpatterns = [
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('save/', SaveSchedule.as_view(), name='save_schedule'),
    path('patch/<str:pk>', PatchSchedule.as_view(), name='patch_schedule')
]

