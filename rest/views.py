# import mixins as mixins
from django.db.models import Count, F, Avg
# from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.mixins import UpdateModelMixin
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from rest.models import Category, Review, Restaurant, Selection, Sale, Rating, Favorite
from rest.permissions import RestaurantPermission
from rest.serializers import RestaurantSerializer, RestaurantDetailSerializer, CategorySerializer, ReviewSerializer, \
     SaleSerializer, SelectionSerializer, MyUserRatingSerializer, FavoritesSerializer
# CreateRatingSerializer


class RestaurantView(ModelViewSet):
    serializer_class = RestaurantSerializer
    serializer_classes = {
        'retrieve': RestaurantDetailSerializer
    }
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'description', ]
    ordering_fields = ['name', 'price', 'rate']
    filterset_fields = ['selection', 'category']
    permission_classes = (RestaurantPermission, )

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        return Restaurant.objects.all().annotate(rating_count=Count('rate__rate'),
                                                 _average_rating=Avg('rate__rate'))

        # queryset = Restaurant.objects.annotate(
        #     rate=F('rating__rate'),
        #     rating_count=Count('rating__rate')
        # ).aggregate(Avg('rating__rate'))
        # return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', ]
    ordering_fields = ['name', ]
    permission_classes = (RestaurantPermission,)

    def get_queryset(self):
        queryset = Category.objects.annotate(
            rest_count=Count('restaurant')
        )
        return queryset


class SelectionView(ModelViewSet):
    serializer_class = SelectionSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', ]
    ordering_fields = ['name', ]
    permission_classes = (RestaurantPermission,)

    def get_queryset(self):
        queryset = Selection.objects.annotate(
            restaurants_count=Count('restaurant')
        )
        return queryset


class SaleView(ModelViewSet):
    serializer_class = SaleSerializer
    lookup_field = 'pk'
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'text', ]
    ordering_fields = ['name', ]
    filterset_fields = ['restaurant', ]
    permission_classes = (RestaurantPermission,)

    def get_queryset(self):
        queryset = Sale.objects.annotate(
            rest_name=F('restaurant__name')
        ).order_by('id')
        return queryset


class MyUserRatingView(ModelViewSet):
    serializer_class = MyUserRatingSerializer
    permission_classes = (RestaurantPermission, )
    queryset = Rating.objects.all()
    lookup_field = 'restaurant'

    def get_object(self):
        obj, created = Rating.objects.get_or_create(user=self.request.user,
                                                    rest_id=self.kwargs['restaurant'])
        return obj


class ReviewView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (RestaurantPermission,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            user=self.request.user,
            restaurant_id=kwargs.get('rest_pk')
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class FavoritesView(APIView):
    serializer_class = FavoritesSerializer
    permission_classes = (RestaurantPermission,)
    queryset = Favorite.objects.all()

    def get(self, request, rest_pk):
        created = Favorite.objects.filter(restaurant_id=rest_pk, user=request.user).exists()
        if created:
            Favorite.objects.filter(
                restaurant_id=rest_pk,
                user=request.user
            ).delete()
            return Response({'success': 'unliked'})
        else:
            Favorite.objects.create(restaurant_id=rest_pk, user=request.user)
            return Response({'success': 'liked'})



from django.shortcuts import render

# Create your views here.
