from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post, Category, Comments
from django.urls import reverse_lazy, reverse
from .forms import AddPostForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import os

class ShowPosts(ListView):
    model=Post
    template_name = 'allposts.html'
    ordering=['-creation_date']
    paginate_by = 5

    def get_context_data(self, *args,**kwargs):
        context=super(ShowPosts,self).get_context_data(*args,*kwargs)
        post_list=[]
        posts = Post.objects.filter(is_highlited=True)
        for post in posts:
            post_list.append(post)
        context["highlited_post"]=post_list
        return context

### Pozwala uzytkownikowi dodac kategorie.Aby dzialalo odblokowac linijke w url i dodac linka w main html
class AddCategoryView(CreateView):
    model=Category
    fields = ['category']
    template_name='add_category.html'
    reverse_lazy('main')


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self,*args, **kwargs):
         context=super(PostDetail,self).get_context_data(*args,**kwargs)
         post = get_object_or_404(Post, id=self.kwargs['pk'])
         total_likes=post.total_likes()
         context["total_likes"] = total_likes

         like_authors=[]
         for i in post.like.values('username'):
             like_authors.append(i)
         like_authors2=[]
         for i in like_authors:
             like_authors2.append(i["username"])
         context["like_authors"]=like_authors2
         return context

class CreatePost(CreateView):
    model=Post
    template_name = 'create_post.html'
    form_class = AddPostForm
    #fields = ['title','tag','author','body']
    reverse_lazy('main')

class DeletePost(DeleteView):
    model=Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('main')

class EditPost(UpdateView):
    model = Post
    #fields = ['title','tag','category','body']
    form_class = AddPostForm
    template_name = 'edit_post.html'
    reverse_lazy('main')

def AddComment(request,pk):
    post=get_object_or_404(Post,pk=pk)
    value = request.POST.get('add_comment')
    new_comment=Comments(body=value, post=post,comment_author=request.user)
    new_comment.save()
    return HttpResponseRedirect(reverse_lazy('post_detail',args=[pk]))

def DeleteComment(request,pk,post_pk):
    comment=get_object_or_404(Comments,pk=pk)
    comment.delete()
    return HttpResponseRedirect(reverse_lazy('post_detail',args=[post_pk]))

def show_categories(request):
    all_categories=Category.objects.all()
    categories_list=[]
    for category in all_categories:
        categories_list.append(category.category)
    categories_list.sort()
    return render(request,'show_categories.html',{'all_categories':categories_list})

def category_detail_list(request,cat):
    category_detail=Post.objects.filter(category=cat.replace('-',' ')).order_by('-creation_date')
    paginator = Paginator(category_detail, 5)
    page_number = request.GET.get('page')
    category_detail = paginator.get_page(page_number)
    return render(request,'category_detail.html',{'category_list':category_detail,'category_name':cat.replace('-',' ')})

def like_post(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    post.like.add(request.user)
    return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))

def dislike_post(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    post.like.remove(request.user)
    return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))

def search(request):
    if request.method=='POST':
      value=request.POST.get('search')
    searched_list=[]
    posts=Post.objects.all()
    for post in posts:
        if (value in post.tag) or (value in post.category):
            searched_list.append(post)
    return render(request,'search.html',{'searched':searched_list})
