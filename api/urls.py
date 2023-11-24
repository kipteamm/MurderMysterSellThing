from django.urls import path

from .views import *


urlpatterns = [
    path('objects/<str:page>', get_objects, name='get_objects'),
    path('object/<str:id>/', get_object, name='get_object'),
    path('object/toggle-wishlist', toggle_wishlist, name='toggle_wishlist'),
    path('object/test', test_game, name='test_game'),
]