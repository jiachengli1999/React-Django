from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
# endpoints, viewsets, name
router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = router.urls # give urls registered in api/leads endpoint