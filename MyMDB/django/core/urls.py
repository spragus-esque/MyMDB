from django.urls import path
from . import views

# matches url patters to core app
app_name = 'core'
# CBV cannot be called (path func req a callable), .as_view(), name var names the path
urlpatterns = [
    path('movies', views.MovieList.as_view(),name='MovieList'),
    path('movie/<int:pk>', views.MovieDetail.as_view(), name='MovieDetail'), #path route strings (param/arg pos 0) can be given angle brackets to give a parm name -- line 9: gives type for param and name (<pk>) to retrieve correct row from DB
]
