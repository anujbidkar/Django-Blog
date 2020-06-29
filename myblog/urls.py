from django.urls import path

from . import views

urlpatterns = [
    path('',views.Homepage.as_view(),name='home'),
    path('new',views.AddPost.as_view(),name='new'),
    path('detailView/<int:pk>',views.ViewDetail.as_view(),name='detailView'),
    path('blog_edit/<int:pk>',views.EditPost.as_view(),name='blog_edit'),
    path('blog_delete/<int:pk>',views.DeletePost.as_view(),name='blog_delete'),
]