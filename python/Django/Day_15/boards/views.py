from django.shortcuts import render,redirect,get_object_or_404
from .forms import BoardForm
from .models import Board
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    boards = Board.objects.all()

    context = {
        'boards':boards
    }
    return render(request,'boards/index.html',context)

@login_required
def new(request):
    # if request.user.is_authenticated:
    #     return redirect('boards:index')
        #로그인 상태에서 새로운 회원가입이나 로그인이 안되게 막는 코드
        
    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            board = form.save(commit=False)
            return redirect('boards:index')


    else:
        form = BoardForm()

    context={
        'form':form
    }
    return render(request,'boards/new.html',context)

def detail(request, b_id):
    board = get_object_or_404(Board,id=b_id)

    context={
        'board':board
    }
    return render(request,'boards/detail.html',context)

def edit(request, b_id):
    board = get_object_or_404(Board,id=b_id)

    if request.user != board.user:
        return redirect('boards:index')

    if request.method =="POST":
        form=BoardForm(request.POST, instance=board)
        if form.is_valid():
            board=form.save()
            return redirect("boards:detail",board.id)
    else:
        form = BoardForm(instance=board)\
       


    context={
        'form':form
    }

    return render(request,'boards/edit.html',context)

def delete(request, b_id):
    board = get_object_or_404(Board,id=b_id)

    if request.user != boards.user:
        return redirect('boards:index')

    if request.method =="POST":
        board.delete()
        return redirect('boards:indext')
    
    return redirect('boards:detail',board.id)

