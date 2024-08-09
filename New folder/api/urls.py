from django.urls import path
# from .views import ItemList, ItemDetail, LocationDetail, LocationList
# from rest_framework import routers

# router = routers.DefaultRouter(trailing_slash=False)
# router.register('location', LocationList)
# router.register('')
from . import views
urlpatterns = [
    # path('location/', LocationList.as_view()),
    # path('location/<int:pk>/', LocationDetail.as_view()),
    # path('', ItemList.as_view()),
    # path('<int:pk>/', ItemDetail.as_view()),
    path("",views.apiindex,name="index"),
    path("anime/<str:doc_ID>/",views.apiindex,name="index"),
    path("<str:collection_ID>/",views.apiindex,name="index"),
]
