from django.contrib import admin

from .models import Article, Article_Group, Article_Group_Link, Article_Layout, Article_Section, Article_Section_Link

class ArticleList(admin.TabularInline):
    model = Article
    extra = 1

class ArticleGroupLinks(admin.TabularInline):
    model = Article_Group_Link
    extra = 1

class ArticleSections(admin.TabularInline):
    model = Article_Section_Link
    extra = 1

class Article_Group_Admin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title"]}),
        ("Article Group Information", {"fields": [ "pub_date", "sort_order", "tile_image"]}),
    ]
    inlines = [ArticleGroupLinks]

class Article_Group_Link_Admin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Article Group Link Information", {"fields": [ "pub_date", "sort_order", "article_group", "article"]}),
    ]

class Article_Admin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title"]}),
        ("Article Information", {"fields": [ "pub_date", "youtube_video", "tile_image", "blog_image", "synopsis"]}),
    ]
    inlines = [ArticleSections]

admin.site.register(Article_Group, Article_Group_Admin)
admin.site.register(Article, Article_Admin)
admin.site.register(Article_Group_Link, Article_Group_Link_Admin)
admin.site.register(Article_Layout)
admin.site.register(Article_Section)
admin.site.register(Article_Section_Link)