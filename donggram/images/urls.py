from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path(
        "", 
        view=views.Feed.as_view(), 
        name="feed"
    ),
    path(
        "<int:image_id>/",
        view=views.ImageDetail.as_view(), 
        name="feed"
    ),
    path(
        "<int:image_id>/like/", # django variable 
        view=views.LikeImage.as_view(), 
        name="like_image"
    ),
    path(
        "<int:image_id>/unlike/", # django variable 
        view=views.UnLikeImage.as_view(), 
        name="like_image"
    ),
    path(
        "<int:image_id>/comments/", # django variable 
        view=views.CommentOnImage.as_view(), 
        name="comment_image"
    ),
    path(
        "<int:image_id>/comments/<int:comment_id>/", # django variable 
        view=views.ModerateComments.as_view(), 
        name="comment_image"
    ),
    path(
        "comments/<int:comment_id>/", # django variable 
        view=views.Comment.as_view(), 
        name="comment"
    ),
    path(
        "search/", # django variable 
        view=views.Search.as_view(), 
        name="search"
    ),
]

#/images/3/like/

#0 create the url and the view
#1 take the id from the url
#2 we want to find an image with this id
#3 we want to create a like for that image