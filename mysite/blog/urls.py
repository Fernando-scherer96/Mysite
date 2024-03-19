from django.urls import path
from blog.views import PostView, PostDetail
from blog import views

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]