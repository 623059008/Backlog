from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from thing import views
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'thing-api', views.ThingViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'backlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^thing/', include('thing.urls', namespace="thing")),
    url(r'^api-auth/', include('rest_framework.urls'))
]
