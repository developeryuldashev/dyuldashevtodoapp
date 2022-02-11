from django.shortcuts import render, redirect
from .models import Task

def index_view(request):
    if request.method== 'POST':
        if request.user.is_authenticated:
            n_task=request.POST.get('task')
            if n_task:
                Task.objects.create(name=n_task)
                return redirect('home_page')
    all_taks=Task.objects.all()
    # print(all_taks)
    return render(request=request, template_name='index.html', context={
        'vazifalar':all_taks
    })

def edit_view(request, id):
    edit_item = Task.objects.get(id=id)
    if request.method=="POST":
        if request.user.is_authenticated:
            n_task = request.POST.get('task')
            edit_item.name=n_task
            edit_item.save()
            return redirect('home_page')
    return  render(request, template_name='edit.html', context={
        'task':edit_item
    })



def delete_task(request, id):
    if request.method=='POST':
        if request.user.is_authenticated:
            delete_item=Task.objects.get(id=id)
            delete_item.delete()
            return redirect('home_page')
    return render(request, template_name='delete.html')


