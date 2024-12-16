from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone

from .models import Article_Group, Article_Group_Link, Article

#def index(request):
#    return HttpResponse("Hello, world. You're at the londonnaturedaybyday index.")

class ArticleGroupsView(generic.ListView):
    template_name = "articles/articlegroups.html"
    context_object_name = "latest_article_group_list"

    def get_queryset(self):
        """
        Return the list of published article groups
        """
        return Article_Group.objects.filter(pub_date__lte=timezone.now()).order_by("sort_order")[ :20
        ]

class ArticleGroupContentsView(generic.ListView):
    model = Article_Group
    template_name = "articles/articlegroupcontents.html"
    context_object_name = "latest_article_group_contents_list"

    def get_queryset(self):
        """
        Return the list of published article groups
        """
        return Article_Group_Link.objects.filter(pub_date__lte=timezone.now(), article_group=self.kwargs['pk']).order_by("sort_order")

class ArticleView(generic.ListView):
    template_name = "articles/article.html"
    context_object_name = "article_contents"

    def get_queryset(self):
        """
        Return the list of published article groups
        """
        return Article.objects.filter(pub_date__lte=timezone.now(), pk=self.kwargs['pk'])