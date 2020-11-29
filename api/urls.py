from django.urls import path
from api import views

urlpatterns = [
    path("<str:query>/", views.get_info),
    path("company/<int:scrip_code>/", views.get_stats),
]