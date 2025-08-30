from django import forms #type: ignore
from .models import Users, Books

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["name", "age", "liked_book_indices"]



class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ["name", "price"]


class QueryForm(forms.Form):
    db = forms.ChoiceField(choices=[
        ('-----', '-----'),
        ('Users', 'Users'),
        ('Books', 'Books'),
    ])
    keyword = forms.ChoiceField(choices=[
        ('-----', '-----'),
        ('User Name', 'User Name'),
        ('Age', 'Age'),
        ('Liked_Book_indices', 'Liked Book Indices'),
        ('Book Name', 'Book Name'),
        ('Price', 'Price'),
    ])
    sign = forms.ChoiceField(choices=[
        ('-----', '-----'),
        ('=', '='),
        ('<', '<'),
        ('>', '>'),
    ])
    search = forms.CharField()

