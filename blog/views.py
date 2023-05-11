from django.shortcuts import render
from .forms import PostForm
from .models import Post
from  django.http import HttpResponse
from  django.http import HttpResponseRedirect


def  Home(request) :
    context={'blogdb':Post.objects.all()}
    return render(request,'blog/home.html',context)

def  About(request) :
    context={}
    return render(request,'blog/about.html',context)

def  PostBlog(request) :
    #print(request.method)

    # POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        #print(form.is_valid())
        # when your form is valid
        if form.is_valid():
            author = form.cleaned_data['author']
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            Post.objects.create(author=author,title=title,text=text)
            return HttpResponseRedirect('/blog/home/')
        # when my form is not valid
        else:
            context = {'form':form}
            return render(request,'blog/post.html',context)
    # GET
    else:
        form = PostForm()
        context={'form':form}
        return render(request,'blog/post.html',context)
