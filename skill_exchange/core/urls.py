from django.urls import path
from .views import skill_list, add_skill, register, send_request,my_requests, update_request

urlpatterns = [
    path('', skill_list, name='skill_list'),
    path('add/', add_skill, name='add_skill'),
    path('accounts/register/', register, name='register'),
    path('request/<int:skill_id>/', send_request, name='send_request'),
    path('my-requests/', my_requests, name='my_requests'),
    path('request/<int:req_id>/<str:action>/', update_request, name='update_request'),
]
