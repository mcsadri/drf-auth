from django.urls import path
from .views import StarshipList, StarshipDetail

urlpatterns = [
    path('', StarshipList.as_view(), name='starship_list'),
    path('<int:pk>/', StarshipDetail.as_view(), name='starship_detail'),
]
