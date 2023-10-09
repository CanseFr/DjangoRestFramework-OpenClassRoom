from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shop.view.views import CategoryViewset, ProductViewset, ArticleViewset

router = routers.SimpleRouter()
router.register('category',  CategoryViewset, basename='category')
router.register('product', ProductViewset, basename='product')
router.register('article', ArticleViewset, basename='article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/category/', CategoryAPIView.as_view()),
    # path('api/product/', ProductAPIView.as_view()),
    # path('api/product/', ProductAPIView.as_view()),

    # Creation d'un routeur
    # Le détail d’une catégorie est également visible en ajoutant son identifiant dans l’URL, par exemple "http: // 127.0 .0 .1: 8000 / api / category / 1 /".
    # La page vous propose alors de réaliser les actions PUT, PATCH(dans l’onglet « Raw data ») et DELETE sur l’entité consultée.
    path('api/', include(router.urls)),
]
