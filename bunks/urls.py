from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>', views.profile, name="profile"),
    path('bunk/', views.bunk, name="bunk"),
]