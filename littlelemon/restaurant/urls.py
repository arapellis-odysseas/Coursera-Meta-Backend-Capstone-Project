from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('api-token-auth/', obtain_auth_token),
    path('booking/', views.BookingViewSet.as_view({'get': 'list'}), name='booking'),
    path('userList/', views.UserViewSet.as_view({'get': 'list'}), name='userView'),
    path('createUser/', views.UserCreateView.as_view(), name='user-create'),


]