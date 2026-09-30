"""定义blogs的URL模式。"""

from  django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    path('study/', views.study, name='study'),


    # 显示图片
    path('image/', views.image, name='image'),

    # 显示所有博客帖子。
    path('blogposts/', views.blogposts, name='blogposts'),
    # 显示某帖子的全部评论。
    path('blogposts/<int:blogpost_id>/', views.blogpost, name='blogpost'),
    # 用于添加新博客帖子的页面。
    path('new_blog/', views.new_blog, name='new_blog'),
    # 用于添加新评论的页面。
    path('new_comment/<int:blogpost_id>/', views.new_comment, name='new_comment'),
    # 用于编辑评论的页面。
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    # 用于编辑博客帖子的页面。
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),

    path('regist/', views.regist, name='regist'),


]
