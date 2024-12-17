import datetime
from django.db import models
from django.utils import timezone

class Article_Group(models.Model):
    #tile_image = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    tile_image = models.ImageField(null=True, blank=True)
    sort_order = models.IntegerField(default=9999) 
    pub_date = models.DateTimeField("date to publish")

    def __str__(self):
        return self.title

class Article(models.Model):
    #tile_image = models.CharField(max_length=200) 
    #blog_image = models.CharField(max_length=200)     
    #synopsis = models.CharField(max_length=1000)
    title = models.CharField(max_length=200)
    youtube_video = models.CharField(max_length=1000, null=True, blank=True)     
    tile_image = models.ImageField(null=True, blank=True)
    blog_image = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField("date to publish")
    synopsis = models.TextField(null=True, blank=True)    

    def __str__(self):
        return self.title

class Article_Group_Link(models.Model):
    name = models.CharField(max_length=200)
    sort_order = models.IntegerField(default=9999) 
    pub_date = models.DateTimeField("date to publish")
    article_group = models.ForeignKey(Article_Group, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Article_Layout(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)     
    def __str__(self):
        return self.name

class Article_Section(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date to publish")
    article_section_content = models.TextField(null=True, blank=True)     
    article_section_image = models.ImageField(null=True, blank=True)
    article_layout = models.ForeignKey(Article_Layout, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Article_Section_Link(models.Model):
    name = models.CharField(max_length=200)
    sort_order = models.IntegerField(default=9999) 
    pub_date = models.DateTimeField("date to publish", auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    article_section = models.ForeignKey(Article_Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name