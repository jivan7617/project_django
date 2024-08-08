
from django.views.generic.base import View
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostCreateForm
from .models import Post

# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        
        context ={
                
        }                     
        #index.html home into templates
        return render(request, 'blog_list.html', context)

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context ={
            'form':form
        }                     
        #index.html home into templates
        return render(request, "blog_create.html",context)
    
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title= form.cleaned_data.get('title')
                content= form.cleaned_data.get('content')
                
                p, created = Post.objects.get_or_create(title=title,content=content)
                p.save()
                return redirect("blog:home")
                       
        context ={
            
        }                     
        #index.html home into templates
        return render(request, "blog_create.html",context)