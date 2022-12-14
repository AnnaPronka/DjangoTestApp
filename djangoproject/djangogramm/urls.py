from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.PostsView.as_view(), name='feed'),
    path('news/', views.NewsFeed.as_view(), name='news_feed'),
    path('user/edit/', views.UserEdit.as_view(), name='user_edit'),
    path('user/follow/', views.follow, name='follow'),
    path('user/unfollow/', views.unfollow, name='unfollow'),
    path('user/<slug:user_slug>/', views.UserView.as_view(), name='user'),
    path('post/create/', views.CreatePost.as_view(), name='create_post'),
    path('post/like/', views.post_like, name='post_like'),
    path('post/unlike/', views.post_unlike, name='post_unlike'),
    path('post/<int:pk>/', views.PostView.as_view(), name='post'),
    path('sign_up/<username>/<key>/', views.set_active, name='set_active'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('noscript/', views.noscript, name='noscript'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
