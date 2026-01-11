from django.urls import path
from .views import skill_list, add_skill, register, send_request

urlpatterns = [
    path('', skill_list, name='skill_list'),
    path('add/', add_skill, name='add_skill'),
    path('accounts/register/', register, name='register'),
    path('request/<int:skill_id>/', send_request, name='send_request'),
]
