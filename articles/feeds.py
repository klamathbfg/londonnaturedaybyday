from django.contrib.syndication.views import Feed
from django.utils import timezone
from django.template.defaultfilters import truncatewords

from articles.models import Article


class RssArticleFeeds(Feed):
    title = "Articles"
    link = "/latestarticles/"
    description = "Recent articles released on LondonNatureDayByDay.com"

    def items(self):
        return Article.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:100]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.synopsis, 300)

    def item_lastupdated(self, item):
        return item.updated_at