from django.db import models
from django.utils.html import format_html

# from tinymce.models import HTMLField  # content me Rich editor ke liye
# Create your models here.

# Blogs ki Category store karne wali class
class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.title
    
    def img_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px;" />'.format(self.image))
    

# Blog Post ki class
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    url=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.title
    
    def img_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px;" />'.format(self.image))
    
    