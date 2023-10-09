from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from shop.models import Category, Product, Article
from shop.serializer.serializers import CategorySerializer, ProductSerializer, ArticleSerializer


class CategoryViewset(ModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()

    # def get(self, *arg, **kwargs):
    #     categories = Category.objects.all()
    #     serializer = CategorySerializer(categories, many= True) # Le  paramètre  many  permet de préciser au Serializer qu’il va devoir générer une liste d’éléments à partir de l’itérable (notre queryset) qui lui est transmis.
    #     return Response(serializer.data) # Pour obtenir les données sérialisées, nous appelons la propriété  data  de notre serializer. Ce sont ces données qui sont utilisées pour construire la réponse.

# TEST
# git pull origin main

class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class ArticleViewset(ModelViewSet):
    serializer_class = ArticleSerializer
    def get_queryset(self):
        return Article.objects.all()
