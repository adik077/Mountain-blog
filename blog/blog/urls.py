from django.urls import path,include
from .views import ShowPosts, PostDetail, DeletePost, EditPost, CreatePost, show_categories, category_detail_list,AddCategoryView, like_post, dislike_post,search,AddComment, DeleteComment
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',ShowPosts.as_view(),name='main'),
    path('article/<int:pk>/',PostDetail.as_view(),name='post_detail'),
    path('create/',CreatePost.as_view(),name='create'),
    path('delete/<int:pk>/',DeletePost.as_view(),name='delete_post'),
    path('edit/<int:pk>/',EditPost.as_view(),name='edit_post'),
    #path('category/',AddCategoryView.as_view(),name='add_category'),
    path('show-category/',show_categories,name='show_categories'),
    path('category-detail-list/<str:cat>/',category_detail_list,name='category_detail_list'),
    path('like/<int:pk>/',like_post,name='like_post'),
    path('dislike/<int:pk>/',dislike_post,name='dislike_post'),
    path('search/',search,name='search'),
    path('add_comment/<int:pk>/',AddComment,name='add_comment'),
    path('delete_comment/<int:pk>/<int:post_pk>',DeleteComment,name='delete_comment'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)