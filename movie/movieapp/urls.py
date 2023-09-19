from django.urls import path

from . import views
app_name='movieapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('moviedetail/<int:movie_id>/',views.moviedetail,name='moviedetail'),
    path('upload',views.upload,name='upload'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]