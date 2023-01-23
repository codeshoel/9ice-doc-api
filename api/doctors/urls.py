from django.urls import path
from .views import (
    stakeholders_list_create_view,
    stakeholders_retrieve_destroy_view
)


urlpatterns = [
    path('', stakeholders_list_create_view),
    path('<int:pk>/', stakeholders_retrieve_destroy_view),
]

