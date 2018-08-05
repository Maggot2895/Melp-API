from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('restaurants',views.RestaurantsView)

urlpatterns = [

    url('',include(router.urls)),
    #url('statistics/(?P<pk>.+)/$', views.RestaurantsView.as_view())
    #print('statistics/(?P<pk>.+)/$')
    #url('^statistics'+'?'+'(P<pk>.+)/$', views.StatisticsView)
    #url(r'^(?P<username>\w{0,50})/$', views.RestaurantsView.profile_page)
    ]