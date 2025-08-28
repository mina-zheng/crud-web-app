from .models import User, Books
from django.shortcuts import render #type:ignore

def index(request):
    books = Books.objects.all()
    users = User.objects.all()

    if request.method == "POST":
        if "delete-book" in request.POST:
            delete(request, "book", Books)
        elif "delete-user" in request.POST:
            delete(request, "user", User)
            

    return render(request, 'crud/index.html', {'books': books,
                                               'users': users})




def delete(request, db, model):
    action = "delete-" + db
    book_name = request.POST.get(action)
    delete_row = model.objects.filter(name=book_name)
    delete_row.delete()
