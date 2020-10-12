from .views import HomeView, EntryView,CreateEntryView
from django.urls import path

urlpatterns = [
    
    path('', HomeView.as_view(), name='blog-home'),
    path('entry/<int:pk>/', EntryView.as_view(), name="blog-detail"),
    path('createentry/', CreateEntryView.as_view(success_url='/'), name="blog-create"),
]
