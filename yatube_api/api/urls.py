from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import (CommentViewSet,
                       GroupViewSet,
                       PostViewSet,
                       FollowViewSet)


router_v1 = DefaultRouter()

router_v1.register('posts',
                   PostViewSet,
                   basename='posts')
router_v1.register('posts/(?P<post_id>\\d+)/comments',
                   CommentViewSet,
                   basename='comments')
router_v1.register('groups',
                   GroupViewSet,
                   basename='groups')
router_v1.register('follow',
                   FollowViewSet,
                   basename='follow'),

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
