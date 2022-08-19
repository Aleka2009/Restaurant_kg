from django.urls import path
from about_us.views import ContactsView, AboutUsView


urlpatterns = [
    path('', AboutUsView.as_view({'get': 'list'})),
    path('contacts/', ContactsView.as_view({'get': 'list'}))
]
