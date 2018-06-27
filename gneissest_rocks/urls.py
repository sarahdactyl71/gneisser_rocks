from django.urls import path

from . import views

urlpatterns = [
#ex /rocks/
    path('', views.index, name='index'),
    #ex /rocks/5/
    path('<int:rock_id>/', views.detail, name='detail'),
    #ex: /rocks/5/results/
    path('<int:rock_id>/results/', views.results, name='results'),
]
