from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', views.home, name="home"),
    path('contacts/', views.contacts, name="contacts"),
    path('watches/', views.watches, name="watches"),
    path('blog/', PostListView.as_view(), name='blog'),
    path('post/<int:pk/>', PostDetailView.as_view(), name='post-detail'),
]
