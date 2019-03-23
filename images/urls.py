from django.urls import path

from images.views import (ImageList)

urlpatterns = [
    path("<int:meetup_id>/images/", ImageList.as_view(), name="images"),

]
