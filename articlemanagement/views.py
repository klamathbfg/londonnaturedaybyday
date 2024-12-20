from django.views import generic
from django.utils import timezone

from articles.models import Article_Group

class homepage(generic.ListView):
    template_name = "articles/homepage.html"
    context_object_name = "latest_article_group_list"

    def get_queryset(self):
        """
        Return the list of published article groups
        """
        return Article_Group.objects.filter(pub_date__lte=timezone.now()).order_by("sort_order")[ :20
        ]