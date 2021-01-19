from django.urls import path
from rest_framework.routers import DefaultRouter

from blog.views import ( EntryViewSet, ListUser, CommentViewSet, SyncConfig, TagViewSet, ViewViewSet,
                        InteractionViewSet )

router = DefaultRouter()

router.register(r'entries', EntryViewSet, basename='entries')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'views', ViewViewSet, basename='views')
router.register(r'interactions', InteractionViewSet, basename='interactions')

urlpatterns = [
    path('me/', ListUser.as_view()),
    path('sync_config/', SyncConfig.as_view()),
] + router.urls
