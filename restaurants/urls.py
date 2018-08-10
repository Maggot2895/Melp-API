from django.conf.urls import url, include
from .views import RestaurantsView,StatisticView
from rest_framework.routers import SimpleRouter,DefaultRouter

router = DefaultRouter()
router.register('restaurants',RestaurantsView)

urlpatterns = [
    url('(?P<coords>.+)/$', StatisticView.as_view()),
    url('',include(router.urls)),  
    ]


