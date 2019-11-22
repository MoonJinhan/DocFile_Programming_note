from django.shortcuts import render,redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from IPython import embed
from django.urls import reverse

# Create your views here.
def index(request):
    #embed()
    aritlces = Article.objects.all()
    context={
        "articles = articles"
    }
    return render(request, 'article/index.html')

def new(request):
    if request.method=="POST":
        # title=request.POST.get('title')
        # content=request.POST.get('content')
        # article=Article()
        # article.title=title
        # article.content=conetent
        # article.save()
        form = ArticleForm(request.POST)
        #embed()
        if form.is_valid(): #유효성검사 이상없으면True 출력
            author=form.save()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title,content=content)

            return redirect('article:index')

        #return redirect('article:index')
    else:
        form = ArticleForm()

    context ={
        "form" : form
        }

    return render(request,'article/new.html',context)

def detail(request, a_id):
    article =Article.objects.get(id=a_id)
    context={
        "article":article
    }
    
    return render(request,'article/detail.html', context)

def edit(request,a_id):
    #article = Article.objects.get(id=a_id)
    article = get_object_or_404(Article,id=a_id)

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content=form.cleaned_data.get('content')
            article.save()
            return redirect(article)
            #return redirect('article:detail',article.id)
    else:
        
        form = ArticleForm(initial=article.__dict__)
        #embed()
    context = {
        'form':form
    }
    return render(request,'article/new.html',context)
    
# def delete(request, a_id):
#     aritcle = Article.objects.get(id=a_id)
#     if request.method == "POST":
#        article.delete()

#         return redirect("aritcle/detail")
#     else:
#         return 

def get_absolute_url(self):
    return reverse('article:detail',args=[self.id])