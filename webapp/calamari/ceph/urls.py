from django.conf.urls import patterns, include, url
from rest_framework import routers
from ceph import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', views.UserViewSet)
router.register(r'cluster', views.ClusterViewSet)

urlpatterns = patterns('',
    url(r'^user/me', views.user_me),
    url(r'^', include(router.urls)),
    url(r'^cluster/(?P<cluster_pk>[0-9]+)/health$', views.Health.as_view(), name='osd-list'),
    url(r'^cluster/(?P<cluster_pk>[0-9]+)/health_counters$', views.HealthCounters.as_view(), name='health-counters'),
    url(r'^cluster/(?P<cluster_pk>[0-9]+)/space$', views.Space.as_view(), name='osd-list'),
    url(r'^cluster/(?P<cluster_pk>[0-9]+)/osd$', views.OSDList.as_view(), name='osd-list'),
    url(r'^cluster/(?P<cluster_pk>[0-9]+)/osd/(?P<osd_id>\d+)$', views.OSDDetail.as_view(), name='osd-detail'),
    url(r'^cluster/(?P<cluster_pk>[0-9]+)/pool$', views.PoolViewSet.as_view({'get': 'list'}), name='pool-list'),
    url(r'^cluster/(?P<cluster_pk>[0-9]+)/pool/(?P<pool_pk>\d+)$', views.PoolViewSet.as_view({'get': 'retrieve'}),
        name='pool-detail'),
    url(r'^cluster/(?P<cluster_pk>[0-9]+)/server', views.ServerViewSet.as_view({'get': 'list'}), name='server-list')
)