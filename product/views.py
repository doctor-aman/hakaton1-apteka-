from django_filters.rest_framework import DjangoFilterBackend
from requests import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from product.filters import ProductFilter
from product.models import Product, Category, Comment, Brand
from product.serializers import ProductSerializer, CommentSerializer, CategorySerializer, BrandSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ['name']  # поиск по имени
    ordering_fields = ['name', 'price']


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentViewSet(GenericViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
