from django.urls import path

from movieinfo_app.views import ActorList

urlpatterns = [

    path('actor/',
         ActorList.as_view(),
         name='actor_list'),
]