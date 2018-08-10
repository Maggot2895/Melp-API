from django.conf.urls import url, include
from .views import RestaurantsView,StatisticView
from rest_framework.routers import SimpleRouter,DefaultRouter

router = SimpleRouter()
router.register(r'restaurants',RestaurantsView)

urlpatterns = [
    url(r'statistics/$', StatisticView.as_view()),
    url('',include(router.urls)),  
    ]


