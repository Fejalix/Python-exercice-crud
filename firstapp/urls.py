from django.urls import path
from . import views
from .views import detail_view
from .views import update_view

app_name = 'firstapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.home_view, name='create'),
    path('list/', views.list_view, name='list'),
    path('<id>', detail_view ),
    path('<id>/update', update_view),
    path('<id>/delete', views.delete_view ),
]