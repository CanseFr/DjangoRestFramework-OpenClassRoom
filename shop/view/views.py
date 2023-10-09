from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from shop.models import Category, Product, Article
from shop.serializer.serializers import CategorySerializer, ProductSerializer, ArticleSerializer


class CategoryViewset(ReadOnlyModelViewSet): # Permet de passer en readOnly
# class CategoryV:iewset(ModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        # return Category.objects.all() # Retourn tout sans contrainte
        queryset = Category.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')

        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset



    # def get(self, *arg, **kwargs):
    #     categories = Category.objects.all()
    #     serializer = CategorySerializer(categories, many= True) # Le  paramètre  many  permet de préciser au Serializer qu’il va devoir générer une liste d’éléments à partir de l’itérable (notre queryset) qui lui est transmis.
    #     return Response(serializer.data) # Pour obtenir les données sérialisées, nous appelons la propriété  data  de notre serializer. Ce sont ces données qui sont utilisées pour construire la réponse.


class ProductViewset(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(active=True) # filtre sur la requete selon champ de l'entité
        category_id = self.request.GET.get('category_id')

        if category_id is not None:
            queryset = queryset.filter(category_id = category_id)

        return queryset


class ArticleViewset(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    def get_queryset(self):
        queryset = Article.objects.filter(active=True)
        article_id = self.request.GET.get('article_id')

        if article_id is not None:
            queryset = queryset.filter(article_id = article_id)

        return queryset
