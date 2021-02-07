from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdate, BookmarkDeleteView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdate.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]