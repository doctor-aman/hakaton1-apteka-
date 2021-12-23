from django.urls import path, include
from rest_framework.routers import SimpleRouter
from product.views import ProductViewSet, CategoryViewSet, CommentViewSet, BrandViewSet

router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('comment', CommentViewSet)
router.register('brand', BrandViewSet)


urlpatterns = [
    path('', include(router.urls))
]