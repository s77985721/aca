from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'Productos', views.ProductoViewSet)
router.register(r'Users', views.UsurioViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('token/', views.CreateTokenView.as_view)

]


