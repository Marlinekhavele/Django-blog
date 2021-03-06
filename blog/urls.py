from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views
from .feeds import LatestPostsFeed


urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path(
        "post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"
    ),
    path(
        "post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"
    ),
    path("about/", views.about, name="blog-about"),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
    path("feed/", LatestPostsFeed(), name="post_feed"),
    path("search/", views.post_search, name="post_search"),
    path("<int:post_id>/add_comment/", views.add_comment, name="add_comment"),
]
