from django.urls import path
from .views import LoginView, HomeView, AddCart, LogoutView, RemoveCart, CartView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add-to-cart/', AddCart.as_view(), name='add_to_cart'),
    path('remove-from-cart/', RemoveCart.as_view(), name='remove_cart'),
    path('view-cart/', CartView.as_view(), name='view_cart'), 
]

