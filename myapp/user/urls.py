from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('taglist/', views.TagListView.as_view(), name='taglistview'),
    path('tagdetail/<int:pk>', views.TagDetailView.as_view(), name='tagdetailview'),
    path('snippets/', views.SnippetListCreateView.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetailedView.as_view(), name='snippet-updated-delete'),
    path('snippetDetailed/<int:pk>/', views.SnippetDetailedView.as_view(), name='snippets-detail'),
    path('overview', views.SnippetOverview.as_view(), name='snippet overview'),

]
