from django.urls import path
from .views import polls_list,polls_details

urlpatterns = [
    path('', polls_list, name='polls_list'),
    path('polls_details/<int:pk>/', polls_details, name='polls_details'),

]