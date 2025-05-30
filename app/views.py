from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Author, Category, Publisher
from .forms import ItemForm, AuthorForm, CategoryForm, PublisherForm

def item_list(request):
    items = Item.objects.all()
    authors = Author.objects.all()
    categories = Category.objects.all()
    publishers = Publisher.objects.all()

    item_form = ItemForm(prefix='item')
    author_form = AuthorForm(prefix='author')
    category_form = CategoryForm(prefix='category')
    publisher_form = PublisherForm(prefix='publisher')

    if request.method == 'POST':
        if 'submit_item' in request.POST:
            item_form = ItemForm(request.POST, prefix='item')
            if item_form.is_valid():
                item_form.save()
                return redirect('item_list')

        elif 'submit_author' in request.POST:
            author_form = AuthorForm(request.POST, prefix='author')
            if author_form.is_valid():
                author_form.save()
                return redirect('item_list')

        elif 'submit_category' in request.POST:
            category_form = CategoryForm(request.POST, prefix='category')
            if category_form.is_valid():
                category_form.save()
                return redirect('item_list')

        elif 'submit_publisher' in request.POST:
            publisher_form = PublisherForm(request.POST, prefix='publisher')
            if publisher_form.is_valid():
                publisher_form.save()
                return redirect('item_list')

    context = {
        'items': items,
        'authors': authors,
        'categories': categories,
        'publishers': publishers,
        'item_form': item_form,
        'author_form': author_form,
        'category_form': category_form,
        'publisher_form': publisher_form,
    }
    return render(request, 'app/item_list.html', context)

# CREATE VIEW

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'app/item_form.html', {'form': form})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = AuthorForm()
    return render(request, 'app/author_form.html', {'form': form})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = CategoryForm()
    return render(request, 'app/category_form.html', {'form': form})

def publisher_create(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = PublisherForm()
    return render(request, 'app/publisher_form.html', {'form': form})

# UPDATE VIEWS

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

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'app/item_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'app/item_form.html', {'form': form})

def publisher_update(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'app/item_form.html', {'form': form})

# DELETE VIEWS

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'app/item_confirm_delete.html', {'item': item})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('item_list')
    return render(request, 'app/item_confirm_delete.html', {'author': author})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('item_list')
    return render(request, 'app/item_confirm_delete.html', {'category': category})

def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('item_list')
    return render(request, 'app/item_confirm_delete.html', {'publisher': publisher})
