"""questioner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns

from tag import views as tag_views
from . import views


api_info = openapi.Info(
    title="Questioner API",
    default_version="v1",
    description=(
        "Crowd-source questions for a meetup. Questioner "
        "helps the meetup organizer prioritize"
        "questions to be answered. Other users can vote "
        "on asked questions and they bubble to the top "
        "or bottom of the log. description"
    ),
    license=openapi.License(name="Andela License"),
)
schema_view = get_schema_view(
    public=True, permission_classes=(permissions.AllowAny,)
)
urlpatterns = [
    path("", views.Index.as_view(), name="welcome"),
    path("accounts/", include('accounts.urls')),
    path("meetups/", include("meetup.urls")),
    path("meetups/", include("question.urls")),
    path("meetups/", include("vote.urls")),
    path("meetups/", include("images.urls")),
    path("tags/", tag_views.TagList.as_view(), name="tags"),
    path("tags/<int:tag_id>", tag_views.ATag.as_view(), name="tag"),
    path("admin/", admin.site.urls),
    path('session/', include('rest_framework.urls', namespace='rest_framework')),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]

format_suffix_patterns(urlpatterns, suffix_required=False, allowed=None)
