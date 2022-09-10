from django.urls import include, path

from cats.views import CatDetail, CatList

urlpatterns = [
    path('cats/', CatList.as_view()),
    path('cats/<int:pk>/', CatDetail.as_view()),
]


