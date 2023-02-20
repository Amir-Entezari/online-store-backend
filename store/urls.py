from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('products', views.ProductViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('collections/', views.CollectionList.as_view()),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(),
         name='collection-detail')
]
