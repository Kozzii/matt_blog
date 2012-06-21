from django.contrib import admin
from models import *

class PostAdmin(admin.ModelAdmin):
	filter_horizontal = ('categories',)
	list_display = ('title', 'published')
	prepopulated_field = {"slug": ("title",)}

admin.site.register(Category)
admin.site.register(Post, PostAdmin)