from django.urls import path
from .import views


urlpatterns = [
    #cart

    path('',views.marketplace,name='marketplace'),
    path('<slug:vendor_slug>/',views.vendor_detail,name='vendor_detail'),
    #add to cart
    path('add_to_cart/<int:food_id>/',views.add_to_cart,name='add_to_cart'),
    # decrease cart
    path('decrease_cart/<int:food_id>/',views.decrease_cart,name='decrease_cart'),
    #delete cart item
    path('delete_car/<int:cart_id>/',views.delete_cart,name='delete_cart')
]
