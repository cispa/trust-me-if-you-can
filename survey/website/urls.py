from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start', views.start, name='start'),
    path('survey/<str:uid>', views.page, name='survey'),
    path('save', views.save, name='save'),
    path('thanks/<str:uid>', views.finish, name='finish'),
]
