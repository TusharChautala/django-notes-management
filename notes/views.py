from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Note
from .forms import NoteForm


# Sign-up view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Signup successful!')
            return redirect('notes_list')
        else:
            messages.error(request, 'Signup failed. Please try again.')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('notes_list')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')


# List notes with pagination
@login_required
def notes_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(notes, 10)  # Show 10 notes per page
    page = request.GET.get('page')
    notes = paginator.get_page(page)
    return render(request, 'notes_list.html', {'notes': notes})


# Create a new note
@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'Note created successfully!')
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})


# Update an existing note
@login_required
def note_update(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect('notes_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_form.html', {'form': form})


# Delete a note
@login_required
def note_delete(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect('notes_list')
    return render(request, 'note_confirm_delete.html', {'note': note})
