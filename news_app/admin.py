from django.contrib import admin

# Register your models here.

from .models import News, Category, Contact, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'news', 'body', 'created_time','active')
    list_filter = ['user', 'news']
    actions = ['enable_comments', 'disable_comments']

    def disable_comments(self, request, queryset):
        queryset.update(active='False')

    def enable_comments(self, request, queryset):
        queryset.update(active='True')


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'published_time']
    list_filter = ['category', 'status']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title','body']
    date_hierarchy = 'published_time'
    ordering = ('published_time', 'status')





class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(News, NewsAdmin)
admin.site.register(Category,CategoryAdmin)

admin.site.register(Contact)

admin.site.register(Comment, CommentAdmin)