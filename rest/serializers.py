from rest_framework import serializers
from rest.models import Category, Selection, Sale, Restaurant, Review, Image, MenuImage, SaleImage, Rating, Favorite, \
    Contact


class SaleImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleImage
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class MenuImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuImage
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'restaurant': {'read_only': True}
        }


class MyUserRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'restaurant': {'read_only': True}
        }

    def create(self, validated_data):
        rate, _ = Rating.objects.update_or_create(
            user=validated_data.get('user', None),
            restaurant_id=validated_data.get('restaurant', None),
            defaults={'rate': validated_data.get("rate")}
        )
        return rate


class CategorySerializer(serializers.ModelSerializer):
    rest_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response = dict(response)
        rest_list = Restaurant.objects.filter(category_id=instance.id).values().order_by('-id')[:4]
        name = response.get('name',)
        id = response.setdefault('id')
        tuple_value = (id, name, rest_list)
        tuple_key = ('id', 'name', 'restaurants')
        dict_cat = dict(zip(tuple_key, tuple_value))
        return dict_cat


# class CategoryDetailSerializer(serializers.ModelSerializer):
#     rest_count = serializers.IntegerField(read_only=True)
#
#     class Meta:
#         model = Category
#         fields = '__all__'


class CategoryFullSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class SelectionSerializer(serializers.ModelSerializer):
    restaurants_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    sale_image = SaleImageSerializer(many=True)
    rest_name = serializers.CharField(read_only=True)

    class Meta:
        model = Sale
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ['user', 'restaurant']

        extra_kwargs = {
            'user': {'read_only': True},
            'restaurant': {'read_only': True}
        }


class RestaurantSerializer(serializers.ModelSerializer):
    phone_numbers = ContactSerializer(many=True)
    liked = serializers.BooleanField(default=False)

    class Meta:
        model = Restaurant
        fields = ['id', 'logo', 'phone_numbers', 'address', 'address_ru', 'address_en',
                  'address_ky', 'instagram', 'liked', 'favorite', 'name_ru', 'name_en', 'name_ky', 'description_ru',
                  'description_en', 'description_ky']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        # fav_list = Favorite.objects.filter(restaurant=instance.id).values_list('restaurant_id', flat=True).first()
        people = response['favorite']
        users = self.context['view'].request.user.id
        if users in people:
            response['liked'] = True
        return response


class RestaurantDetailSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    menu_image = MenuImageSerializer(many=True)
    phone_numbers = ContactSerializer(many=True)
    rate = MyUserRatingSerializer(many=True)
    rating_count = serializers.IntegerField(read_only=True)
    _average_rating = serializers.DecimalField(read_only=True, max_digits=2, decimal_places=1)
    review = ReviewSerializer(many=True)
    liked = serializers.BooleanField(default=False)
    selection = SelectionSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        print(instance)
        # fav_list = Favorite.objects.filter(restaurant=instance.id).values_list('restaurant_id', flat=True).first()
        people = response['favorite']
        users = self.context['view'].request.user.id
        if users in people:
            response['liked'] = True
        return response

