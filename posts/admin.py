from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_link', 'created_at')
    list_filter = ('created_at',)

    def author_link(self, obj):
        author = obj.author
        url = reverse('admin:users_user_changelist') + str(author.pk)
        return format_html(f'<a href="{url}">{author}</a>')

    author_link.short_description = 'Автор'


admin.site.register(Post, PostAdmin)
