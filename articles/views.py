from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone

from .models import Article_Group

#def index(request):
#    return HttpResponse("Hello, world. You're at the londonnaturedaybyday index.")

class IndexView(generic.ListView):
    template_name = "articles/index.html"
    context_object_name = "latest_article_group_list"

    def get_queryset(self):
        """
        Return the list of published article groups
        """
        return Article_Group.objects.filter(pub_date__lte=timezone.now()).order_by("sort_order")[ :20
        ]