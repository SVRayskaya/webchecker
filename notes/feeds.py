from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostsFeed(Feed):
    title = 'My blog'
    link = '/feed/'
    description = 'Новые статьи в блоге.'

    def items(self):
        return Post.published.all()[:2]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)

    def item_link(self, item):
        return item.get_absolute_url()