from django.urls import path, include
from rest.views import ReviewView, RestaurantView, CategoryView, SelectionView, SaleView, MyUserRatingView, \
    FavoritesView, FavView

urlpatterns = [
    path('', RestaurantView.as_view({'get': 'list'})),
    path('<int:pk>/', RestaurantView.as_view(
        {'get': 'retrieve'}
    )),
    path('category/', CategoryView.as_view({'get': 'list'})),
    path('selection/', SelectionView.as_view({'get': 'list'})),
    path('sale/', SaleView.as_view({'get': 'list'})),
    path('<int:re_pk>/rating/', MyUserRatingView.as_view({'post': 'create'})),
    path('<int:rest_pk>/review/create/', ReviewView.as_view({'post': 'create'})),
    path('<int:rest_pk>/favorites/', FavoritesView.as_view()),
    path('favorites/', FavView.as_view({'get': 'list'})),
]
