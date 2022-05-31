from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect_path/', views.redirect_path, name='redirect path'),
    path('redirect_page/<int:value_int>/<slug:value_str>', views.redirect_page, name='redirect page'),
]
