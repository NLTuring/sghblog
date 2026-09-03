from django.shortcuts import render,HttpResponse,reverse,redirect
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_POST,require_GET
from django.core.paginator import Paginator
import bleach
from .models import *
from .forms import  PubBlogForm
from django.http.response import  JsonResponse
from django.db.models import Q
# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)
    page = paginator.get_page(request.GET.get('page'))
    return render(request,'index.html',context={"page_obj": page})


def blog_detail(request,blog_id):
    try:
        blog=Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return render(request,'404.html', status=404)
    return render(request,'blog_detail.html',context={"blog":blog})

@require_http_methods(['GET','POST'])
@login_required(login_url=reverse_lazy("sghauth:login"))
def pub_blog(request):
    if request.method == 'GET':
        categories=BlogCategory.objects.all()
        return render(request,'pub_blog.html',context={"categories":categories})
    else:
        form = PubBlogForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data.get('title')
            content=form.cleaned_data.get('content')
            category_id=form.cleaned_data.get('category')
            if not BlogCategory.objects.filter(pk=category_id).exists():
                return JsonResponse({"code":400,"message":"分类不存在!"})
            blog=Blog.objects.create(title=title,content=content,category_id=category_id,author=request.user)
            return JsonResponse({"code":200,"message":"博客发布成功!","data":{"blog_id":blog.id}})
        else:
            print(form.errors)
            return JsonResponse({"code":400,"message":"参数错误!"})


#必须是post请求且必须登录才能调用该视图函数
@require_POST
@login_required(login_url=reverse_lazy("sghauth:login"))
def pub_comment(request):
        blog_id=request.POST.get('blog_id')
        content=request.POST.get('content')
        BlogComment.objects.create(blog_id=blog_id,content=content,author=request.user)
        #重新加载博客详情页
        return redirect(reverse("blog:blog_detail",kwargs={"blog_id":blog_id}))


@require_GET
def search(request):
    q=request.GET.get('q')
    blogs=Blog.objects.filter(Q(title__icontains=q) | Q(content__icontains=q)).all()
    paginator = Paginator(blogs, 5)
    page = paginator.get_page(request.GET.get('page'))
    return render(request,'index.html',context={"page_obj": page})