from django.shortcuts import render
from .models import Article
from rest_framework import viewsets
from rest_framework import permissions
from info.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-date')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]
# Create your views here.
