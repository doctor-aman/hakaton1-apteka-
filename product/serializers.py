from rest_framework import serializers

from product.models import Product, Category, Brand, Comment, GroupProduct


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'brand')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class GroupProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupProduct
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['product', 'text', 'rating']

        def validate_rating(self, rating):
            if rating not in range(1, 6):
                raise serializers.ValidationError('Рейтинг должен быть от 1 до 5')
            return rating
