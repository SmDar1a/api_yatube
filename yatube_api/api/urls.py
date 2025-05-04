from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework import routers
from .views import (
    GroupView,
    GroupDetailView,
    PostViewSet,
    CommentViewSet,
)

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment',
)

urlpatterns = [
    path(
        route='api-token-auth/',
        view=views.obtain_auth_token,
        name='api_token',
    ),
    path(
        route='groups/',
        view=GroupView.as_view(),
        name='api_groups',
    ),
    path(
        route='groups/<int:pk>/',
        view=GroupDetailView.as_view(),
        name='change_group_state',
    ),
    path(
        route='',
        view=include(router.urls),
        name='api_base_url',
    ),
]
