from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Author
from .forms import ItemForm, AuthorForm

def item_list(request):
    items = Item.objects.all()
    return render(request, 'app/item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'app/item_form.html', {'form': form})

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'app/item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'app/item_confirm_delete.html', {'item': item})

# ============================================ CRUD Author

def autor_list(request):
    autor = Author.objects.all()
    return render(request, 'app/item_list.html', {'autor': autor})

def autor_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = AuthorForm()
    return render(request, 'app/item_form.html', {'autor': autor})

def autor_update(request, pk):
    autor = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = AuthorForm(instance=autor)
    return render(request, 'app/item_form.html', {'autor': autor})

def autor_delete(request, pk):
    autor = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('item_list')
    return render(request, 'app/item_confirm_delete.html', {'autor': autor})
