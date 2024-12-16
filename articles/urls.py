from django.urls import path

from . import views

urlpatterns = [
    path("", views.ArticleGroupsView.as_view(), name="articlegroups"),
    path("<int:pk>/", views.ArticleView.as_view(), name="articlecontents"),
    path("grouping/<int:pk>/", views.ArticleGroupContentsView.as_view(), name="articlegroupcontents"),
]