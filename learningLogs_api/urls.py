
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from Logs.views import EntryAPIList, EntryAPIUpdate, TopicWithEntry, TopicAPIList, TopicAPIUpdate

router = routers.DefaultRouter()
router.register(r'women', TopicWithEntry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/Topiclist', TopicAPIList.as_view()),
    path('api/v1/Topic/<int:pk>/', TopicAPIUpdate.as_view()),
    path('api/v1/Entrylist', EntryAPIList.as_view()),
    path('api/v1/Entry/<int:pk>/', EntryAPIUpdate.as_view()),
    path('api/v1/EntryDelete/<int:pk>/', EntryAPIUpdate.as_view()),
    # path('api/v1/EntryTopic/<int:pk>/', TopicWithEntry.as_view()),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
