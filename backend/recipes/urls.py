from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipes.views import IngredientsViewSet, RecipeViewSet, TagsViewSet

router_v1 = DefaultRouter()
router_v1.register(r'recipes', RecipeViewSet, basename='recipes')
router_v1.register(r'ingredients', IngredientsViewSet, basename='ingredients')
router_v1.register(r'tags', TagsViewSet, basename='tags')


urlpatterns = [
    path('', include(router_v1.urls)),
]
