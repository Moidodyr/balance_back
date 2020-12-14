from .models import Article
from .serializers import ArticleListSerializer
from rest_framework import generics


class ArticleListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
