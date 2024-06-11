from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item
# home_page = None
def home_page(request):
    # if request.method == 'POST':
    #     # new_item_text = request.POST.get('item_text','')
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-new-page/')
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {
        'items': items
    })
def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-new-page/')
# Create your views here.
