from rest_framework import routers, viewsets
from ecodrinks.models import Cocktail
from ecodrinks.serializers import CocktailSerializer

class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

router = routers.DefaultRouter()
router.register(r'cocktail', CocktailViewSet, basename='cocktail')

urlpatterns = router.urls