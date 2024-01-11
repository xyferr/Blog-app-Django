from django.contrib import admin
from .models import Category,Post

# Register your models here.

# Category admin ka configuration
class CategoryAdmin(admin.ModelAdmin):
    list_display=('img_tag','title','description','url','image','add_date',)
    search_fields=('title',)

class PostAdmin(admin.ModelAdmin):
    list_display=('img_tag','title','url','category','image','add_date',)
    search_fields=('title',)
    list_filter=('category',)
    
    class Media:
        js=('https://cdn.tiny.cloud/1/nsp8hv1tf9b0vofetq3ik8o6t9m3ff09l6x4g7hqa03jucq8/tinymce/5/tinymce.min.js','js/script.js')
        
        

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)

