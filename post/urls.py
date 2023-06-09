"""
Establishing URL pathways accessible for specific posts
"""
from django.urls import path
from post.views import index, new_post, post_details, tags, like, favorite, new_plant # pylint: disable=E0401


urlpatterns = [
   	path('', index, name='index'),
   	path('newpost/', new_post, name='newpost'),
   	path('<uuid:post_id>', post_details, name='postdetails'),
   	path('<uuid:post_id>/like', like, name='postlike'),
   	path('<uuid:post_id>/favorite', favorite, name='postfavorite'),
   	path('tag/<slug:tag_slug>', tags, name='tags'),
    path('newplant/', new_plant, name='newplant')]
