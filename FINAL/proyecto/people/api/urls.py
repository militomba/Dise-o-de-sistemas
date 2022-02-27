from rest_framework import routers
from .views import UsuariosViewSets

router = routers.SimpleRouter()
router.register(r'persona', UsuariosViewSets, basename='persona')
urlpatterns = router.urls