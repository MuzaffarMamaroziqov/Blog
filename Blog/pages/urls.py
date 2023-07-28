from django.urls import path
from .views import BlogListView
from .views import BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView

urlpatterns=[
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete_post'),
    path('post/<int:pk>/edit',BlogUpdateView.as_view(),name='post_update'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='detail_list')

]