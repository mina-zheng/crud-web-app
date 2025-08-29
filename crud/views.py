from .models import Users, Books
from .forms import UsersForm, BooksForm, QueryForm
from django.shortcuts import render, redirect #type:ignore

def index(request):
    if request.method == "POST":
        if "delete-book" in request.POST:
            delete(request, "book", Books)
        elif "delete-user" in request.POST:
            delete(request, "user", Users)

        elif "add-book" in request.POST:
            add(request, "book", Books)
        elif "add-user" in request.POST:
            add(request, "user", Users)

        return redirect("index")

    books = Books.objects.all()
    users = Users.objects.all()


    return render(request, 'crud/index.html', {'books': books,
                                                'users': users,
                                                'users_form':UsersForm(),
                                                'books_form':BooksForm(),
                                                'query_form':QueryForm()
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