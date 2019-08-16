from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^profile/',views.profile,name ='profile'),
    url(r'^profile_update/',views.update_profile,name='profile_update'),
]