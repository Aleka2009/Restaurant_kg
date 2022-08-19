from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from about_us.serializers import AboutUsSerializer, ContactsSerializer
from about_us.models import AboutUs, Contacts


class AboutUsView(ModelViewSet):
    serializer_class = AboutUsSerializer
    queryset = AboutUs.objects.all()


class ContactsView(ModelViewSet):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
