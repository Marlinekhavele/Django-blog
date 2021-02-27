from django.urls import path
from blog.api.views import api_detail_post_view

app_name = "blog"

urlpatterns = [
    path('<int:pk>/',api_detail_post_view,name="detail"),
]

