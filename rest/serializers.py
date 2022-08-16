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
        fields = ['rate', 'restaurant', 'user']

# class CreateRatingSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Rating
#         fields = ["user", "star", "restaurant"]

    # def create(self, validated_data):
    #     rating = Rating.objects.update_or_create(
    #         user=validated_data.get('user', None),
    #         restaurant=validated_data.get('restaurant', None),
    #         defaults={'star': validated_data.get("star")}
    #     )
    #     return rating


class CategorySerializer(serializers.ModelSerializer):
    rest_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'rest_count', ]


class SelectionSerializer(serializers.ModelSerializer):
    restaurants_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Selection
        fields = ['id', 'name', 'image', 'restaurants_count', ]


class SaleSerializer(serializers.ModelSerializer):
    sale_image = SaleImageSerializer(many=True)
    rest_name = serializers.CharField(read_only=True)

    class Meta:
        model = Sale
        fields = ['id', 'time_create', 'time_update', 'name', 'sale_image', 'text', 'rest_name', ]


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    phone_numbers = ContactSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'logo', 'phone_numbers',
                  'address', 'instagram', ]


class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ['user', 'restaurant']


class RestaurantDetailSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    menu_image = MenuImageSerializer(many=True)
    phone_numbers = ContactSerializer(many=True)
    rate = MyUserRatingSerializer(many=True)
    rating_count = serializers.IntegerField(read_only=True)
    _average_rating = serializers.DecimalField(read_only=True, max_digits=2, decimal_places=1)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description', 'image', 'phone_numbers',
                  'address', 'openning_times', 'menu_image', 'rate', '_average_rating', 'rating_count',
                  'site']



