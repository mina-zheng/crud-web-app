from .models import Users, Books
from .forms import UsersForm, BooksForm, QueryForm
from django.shortcuts import render, redirect #type:ignore

def index(request):
    res, db = None, None
    if request.method == "POST":
        if "delete-book" in request.POST:
            delete(request, "book", Books)
            return redirect("index")
        elif "delete-user" in request.POST:
            delete(request, "user", Users)
            return redirect("index")
        elif "add-book" in request.POST:
            add(request, "book", Books)
            return redirect("index")
        elif "add-user" in request.POST:
            add(request, "user", Users)
            return redirect("index")
        
        elif "show-books" in request.POST:
            indices = request.POST.get("show-books")
            indices_list = indices.split()
            
            liked = Books.objects.filter(id__in=indices_list)

        elif "query" in request.POST:
            form = QueryForm(request.POST)
            if form.is_valid():
                db = form.cleaned_data['db']
                keyword = form.cleaned_data['keyword']
                sign = form.cleaned_data['sign']
                search = form.cleaned_data['search']

                keyword_map = {
                    'User Name': 'Name',
                    'Book Name': 'Name',
                    'Liked Book Indices': 'liked_book_indices'
                }
                if keyword in keyword_map:
                    keyword = keyword_map[keyword]

                if sign == "=":
                    lookup = keyword
                elif sign == ">":
                    lookup = keyword + "__gt"
                elif sign == "<":
                    lookup = keyword + "__lt"

                lookup = lookup.lower()
                
                if db == "Books":
                    res = Books.objects.filter(**{lookup: search})
                elif db == "Users":
                    res = Users.objects.filter(**{lookup: search})

    books = Books.objects.all()
    users = Users.objects.all()


    return render(request, 'crud/index.html', {'books': books,
                                                'users': users,
                                                'users_form':UsersForm(),
                                                'books_form':BooksForm(),
                                                'query_form':QueryForm(),
                                                'res':res if res else None,
                                                'db': db,
                                                'liked': liked
                                                })




def delete(request, db, model):
    action = "delete-" + db
    book_name = request.POST.get(action)
    delete_row = model.objects.filter(name=book_name)
    delete_row.delete()

def add(request, db, model):
    if db == "book":
        row = BooksForm(request.POST)
        if row.is_valid():
            row.save()            
    if db == "user":
        row = UsersForm(request.POST)
        if row.is_valid():
            row.save() 