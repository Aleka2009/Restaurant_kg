from django.urls import path, include
from rest.views import ReviewView, RestaurantView, CategoryView, SelectionView, SaleView, MyUserRatingView, \
    FavoritesView

urlpatterns = [
    path('', RestaurantView.as_view({'get': 'list'})),
    path('<int:pk>/', RestaurantView.as_view(
        {'get': 'retrieve'}
    )),
    path('category/', CategoryView.as_view({'get': 'list'})),
    path('selection/', SelectionView.as_view({'get': 'list'})),
    path('sale/', SaleView.as_view({'get': 'list'})),
    path('rating/', MyUserRatingView.as_view({'post': 'create'})),
    path('<int:rest_pk>/review/create/', ReviewView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:rest_pk>/favorites/', FavoritesView.as_view()),
]
