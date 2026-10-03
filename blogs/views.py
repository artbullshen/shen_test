from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
from .models import BlogPost, Comment, Students
from .forms import BlogForm, CommentForm

# 加载图片模型
from .models import Test
import datetime

def index(request):
    """阿特牛的博客主页."""
    now = datetime.datetime.now()
    context = {'now':now}
    return render(request, 'blogs/index.html', context)

# 定义图片加载视图并传送参数items给模板文件my_image_test。
def image(request):
    now = datetime.datetime.now()    
    items = Test.objects.all()
    context = {'now':now, 'items':items}
    return render(request, 'blogs/my_image_test.html', context)


def study(request):
    """研究模型字段增加，以及图形文件的添加。"""
    stu = Students.objects.order_by('id')
    context = {'stu':stu }

    return render(request, 'blogs/study.html', context)


def blogposts(request):
    """显示所有的帖子。"""
    blogposts = BlogPost.objects.order_by('-date_added')
    context = {'blogposts':blogposts}
    return render(request, 'blogs/blogposts.html', context)


@login_required
def blogpost(request, blogpost_id):
    """显示具体某一条博客及其评论。"""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    # 确认请求的博客属于当前用户。
    if blogpost.owner != request.user:
        raise Http404
    comments = blogpost.comment_set.order_by('-date_added')
    context = {'blogpost':blogpost, 'comments':comments}
    return render(request, 'blogs/blogpost.html', context)

@login_required
def new_blog(request):
    """添加新博客帖子。"""
    if request.method != 'POST':
        # 未提交数据，创建一个新表单。
        form = BlogForm()
    else:
        # POST提交的数据：对数据进行处理。
        form =BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blogposts')

    # 显示空表单或指出表单数据无效。
    context = {'form':form}
    return render(request,'blogs/new_blog.html', context)

@login_required
def new_comment(request, blogpost_id):
    """在特定博客中添加新评论。"""
    blogpost = BlogPost.objects.get(id=blogpost_id)

    if request.method != 'POST':
        # 未提交数据，创建一个空表单。
        form = CommentForm()
    else:
        # POST提交的数据：对数据进行处理。
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blogpost = blogpost
            new_comment.save()
            return redirect('blogs:blogpost', blogpost_id=blogpost_id)

    # 显示空表单或指出表单数据无效。
    context = {'blogpost':blogpost, 'form': form}
    return render(request,'blogs/new_comment.html', context)

@login_required
def edit_comment(request, comment_id):
    """编辑既有评论。"""
    comment = Comment.objects.get(id=comment_id)
    blogpost = comment.blogpost

    if blogpost.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求：使用当前评论填充表单。
        form = CommentForm(instance=comment)
    else:
        # POST提交的数据：对数据进行处理。
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogpost', blogpost_id=blogpost.id)

    context = {'comment':comment, 'blogpost':blogpost, 'form':form}
    return render(request, 'blogs/edit_comment.html', context)

@login_required
def edit_blog(request, blog_id):
    """编辑指定id的帖子的页面。"""
    blogpost = BlogPost.objects.get(id=blog_id)

    if blogpost.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求：使用当前帖子填充表单。
        form = BlogForm(instance=blogpost)
    else:
        # POST提交的数据：
        form =BlogForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogpost', blogpost_id=blogpost.id)

    context = {'blogpost':blogpost, 'form':form}
    return render(request, 'blogs/edit_blog.html', context)

def regist(request):
    try:
        post = request.POST
        account = post.get('account')
        if Students.objects.filter(account=account):
            return render(request, 'regist.html', {'msg':'帐号已存在！'})
        password = post.get('pwd1')
        p2 = post.get('pwd2')
        if password != p2:
            return render(request, 'regist.html', {'msg':'两次密码不一致'})
        name = post.get('name')
        gradeclass = post.get('gradeclass')
        password = md5(password.encode()).hexdigest()
        s = Students(account=account, password=password,name=name, gradeClass=gradeclass)
        s.save()
        return render(request, 'regist.html', {'msg':'注册成功'})

    except:
        return render(request, 'regist.html', {'msg':None})




