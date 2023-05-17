from django import forms
from .models import Book, ReadingList

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'cover_image', 'published_date']

class ReadingListForm(forms.ModelForm):
    class Meta:
        model = ReadingList
        fields = ['read', 'to_read']