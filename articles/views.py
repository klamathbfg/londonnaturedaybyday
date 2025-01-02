from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.db.models.functions import ExtractMonth, ExtractDay

from .models import Article_Group, Article_Group_Link, Article, Article_Section, Article_Section_Link

class ArticleGroupsView(generic.ListView):
    template_name = "articles/articlegroups.html"
    context_object_name = "latest_article_group_list"

    def get_queryset(self):
        return Article_Group.objects.filter(pub_date__lte=timezone.now()).order_by("sort_order")[ :20]

class ArticleGroupContentsView(generic.ListView):
    model = Article_Group
    template_name = "articles/articlegroupcontents.html"
    context_object_name = "latest_article_group_contents_list"

    def get_queryset(self):
        return Article_Group_Link.objects.filter(article_group=self.kwargs['pk']).order_by("sort_order")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_article_group_list'] = Article_Group.objects.filter(pub_date__lte=timezone.now()).order_by("sort_order")[ :20]
        context['This_Article_Group'] = Article_Group.objects.filter(pk=self.kwargs['pk'])
        return context

class ArticleView(generic.ListView):
    model=Article
    template_name = "articles/article.html"
    context_object_name = "article_contents"

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_article_group_list'] = Article_Group.objects.filter(pub_date__lte=timezone.now()).order_by("sort_order")[ :20]
        article_sections = Article_Section.objects.filter(pub_date__lte=timezone.now(),article_section_link__article_id=self.kwargs['pk'])[:20]
        """article_sections = Article_Section.objects.filter(pub_date__lte=timezone.now(),
                                                          article_section_link__article_id=self.kwargs['pk']).annotate(section_sort_order=('article_section_link__sort_order')).order_by('section_sort_order')[:20]"""
        context['latest_article_sections_list'] = article_sections
        return context    
    
class Today(generic.ListView):
    model=Article
    template_name = "articles/today.html"
    context_object_name = "article_contents"

    def get_queryset(self):
        today = timezone.now()
        return Article.objects.filter(pub_date__month=today.month, pub_date__day=today.day) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_article_group_list'] = Article_Group.objects.filter(pub_date__lte=timezone.now()).order_by("sort_order")[ :20]
        return context    