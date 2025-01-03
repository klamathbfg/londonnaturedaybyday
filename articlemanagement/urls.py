from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from articles import feeds

from . import views

with open("/home/londonnaturedaybyday/articlemanagement/static/index.html", 'r', encoding='utf-8') as inputfile:
    homepage=inputfile.readlines()

urlpatterns = [
    path('articles/', include("articles.urls")),
    path('admin/', admin.site.urls),
    path('', views.homepage.as_view(), name="Home-Page"),
    path("feed/rss/", feeds.RssArticleFeeds(), name="articles_feed")
]