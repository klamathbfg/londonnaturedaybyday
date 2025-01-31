from django.contrib.syndication.views import Feed
from django.utils import timezone
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatewords

from articles.models import Article


class RssArticleFeeds(Feed):
    title = "London Nature Day By Day"
    link = "/latestarticles/"
    description = "Recent articles released on LondonNatureDayByDay.com"

    def items(self):
        return Article.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:400]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        description = format_html(
            "<img src='https://www.londonnaturedaybyday.com/media/{}'/>{}",
            item.tile_image,
            truncatewords(item.synopsis, 300))
        return mark_safe(f"{description}")
    
    def item_lastupdated(self, item):
        return item.updated_at