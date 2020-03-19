from django.urls import path
from . import views


#application namespace
app_name = 'forum'


urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('post/new', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:post_id>/comment', views.CommentView.as_view(), name='comment')
]
