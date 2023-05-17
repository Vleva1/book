from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Book, Friendship, ReadingList
from .forms import BookForm, ReadingListForm


@login_required
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

@login_required
def add_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        reading_list_form = ReadingListForm(request.POST)
        if book_form.is_valid() and reading_list_form.is_valid():
            book = book_form.save()
            reading_list = reading_list_form.save(commit=False)
            reading_list.user = request.user
            reading_list.book = book
            reading_list.save()
            return redirect('reading_list')
    else:
        book_form = BookForm()
        reading_list_form = ReadingListForm()
    return render(request, 'add_book.html', {'book_form': book_form, 'reading_list_form': reading_list_form})

@login_required
def reading_list(request):
    user = request.user
    reading_list = ReadingList.objects.filter(user=user)
    return render(request, 'reading_list.html', {'reading_list': reading_list})

@login_required
def add_to_reading_list(request, book_id):
    user = request.user
    book = get_object_or_404(Book, id=book_id)
    reading_list, created = ReadingList.objects.get_or_create(user=user, book=book)
    if created:
        messages.success(request, f'{book.title} added to your reading list!')
    else:
        messages.warning(request, f'{book.title} is already in your reading list!')
    return redirect('home')

@login_required
def mark_as_read(request, book_id):
    user = request.user
    book = get_object_or_404(Book, id=book_id)
    reading_list = get_object_or_404(ReadingList, user=user, book=book)
    reading_list.read = True
    reading_list.to_read = False
    reading_list.save()
    messages.success(request, f'{book.title} marked as read!')
    return redirect('reading_list')

@login_required
def mark_as_to_read(request, book_id):
    user = request.user
    book = get_object_or_404(Book, id=book_id)
    reading_list = get_object_or_404(ReadingList, user=user, book=book)
    reading_list.read = False
    reading_list.to_read = True
    reading_list.save()
    messages.success(request, f'{book.title} marked as to read!')
    return redirect('reading_list')

@login_required
def friends(request):
    user = request.user
    friends = Friendship.objects.filter(user=user)
    return render(request, 'friends.html', {'friends': friends})

@login_required
def add_friend(request, friend_id):
    user = request.user
    friend = get_object_or_404(User, id=friend_id)
    friendship, created = Friendship.objects.get_or_create(user=user, friend=friend)
    if created:
        messages.success(request, f'{friend.username} added to your friends!')
    else:
        messages.warning(request, f'{friend.username} is already your friend!')
    return redirect('friends')

@login_required
def friend_reading_list(request, friend_id):
    friend = get_object_or_404(User, id=friend_id)
    reading_list = ReadingList.objects.filter(user=friend, read=True)
    return render(request, 'friend_reading_list.html', {'friend': friend, 'reading_list': reading_list})