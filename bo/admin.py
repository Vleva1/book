from django.contrib import admin

from .models import Book, Friendship, ReadingList

admin.register(Book)
admin.register(Friendship)
admin.register(ReadingList)