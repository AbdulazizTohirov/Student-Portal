from django import views
from django.urls import path
from . import views
urlpatterns = [
    # home page
    path('', views.home, name="home"),

    # notes page
    path('notes',views.notes, name="notes_url"),
    path('delete/notes/<int:pk>',views.delete_note, name="delete-note"),
    path('notes/detail/<int:pk>',views.NotesDetailView.as_view(), name="notes-detail"),

    # homework page
    path('homework',views.homework, name="homework_url"),
    path('update/homework/<int:pk>',views.update_homework, name="update-homework"),
    path('delete/homework/<int:pk>',views.delete_homework, name="delete-homework"),

    # youtube page 
    path('youtube/',views.youtube,name='youtube_url'),

    # To do page
    path('todo/',views.todo,name='todo_url'),
    path('update/todo/<int:pk>',views.update_todo, name="update-todo"),
    path('delete/todo/<int:pk>',views.delete_todo, name="delete-todo"),

    # Books Page
    path('books',views.books,name='books_url'),

    # Dictionary Page
    path('dictionary',views.dictionary,name='dictionary_url'),

    # Wiki
    path('wiki',views.wiki,name='wiki_url'),

    # Conversion
    path('conversion',views.conversion,name='conversion_url'),

    # Profil
    path('profile',views.profile,name='profile_url'),

    # Logout
    path('logout',views.logout,name='logout_url'),


]
