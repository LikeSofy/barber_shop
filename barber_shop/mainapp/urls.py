from django.urls import path

from .views import index_controller, services_controller, masters_controller, master_controller, login_controller, \
    register_controller, logout_controller

urlpatterns = [
    path('', index_controller, name='index'),
    path('services/', services_controller, name='services'),
    path('masters/', masters_controller, name='masters'),
    path('masters/<int:master_id>/', master_controller, name='master'),
    path('register/', register_controller, name='register'),
    path('login/', login_controller, name='login'),
    path('logout/', logout_controller, name='logout'),
    # url(r'^logout/$', do_logout, name='logout'),
    # url(r'^appointment/$', view_cart, name='view_cart'),
    # url(r'^my-appointment/$', view_cart, name='view_cart'),
]
