from django.urls import path
from blog.api import views

app_name = "blog"

urlpatterns = [
    path('blog/', views.posts_list),
    path('blog/<int:pk>/', views.posts_details),
    path('comment/', views.comments_list),
    path('comment/<int:pk>/', views.comments_details),


   

   

]

