from django.urls import path, include # type: ignore

from productapp.views import * # type: ignore

urlpatterns = [
    path('index/', home_view, name='index' ),
    path('insert/', insert_view, name='insert' ),
    path('productapp/display/', display_view, name='display' ),
    path('delete/<int:product_id>/', delete_view),
    path('update/<int:product_id>/', update_view),
    path('register/',register_view,name="register"),
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
]