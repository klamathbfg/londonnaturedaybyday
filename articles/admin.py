from django.contrib import admin

from .models import Article, Article_Group, Article_Group_Link, Article_Layout, Article_Section, Article_Section_Link

admin.site.register(Article_Group)
admin.site.register(Article)
admin.site.register(Article_Group_Link)
admin.site.register(Article_Layout)
admin.site.register(Article_Section)
admin.site.register(Article_Section_Link)