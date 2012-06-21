from django.conf.urls.defaults import *
from django.views.generic import list_detail
from models import Post
 
urlpatterns = patterns('',
	url(r'^$', list_detail.object_list, {'queryset': Post.objects.order_by('-published'), 'template_object_name': 'post',}, name="blog_home"),
	url(r'^post/(?P<object_id>\d+)/$', list_detail.object_detail, {'queryset': Post.objects.all(), 'template_object_name': 'post',}, name="single_post"),
)