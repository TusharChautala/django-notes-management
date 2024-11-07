from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.notes_list, name='notes_list'),
    path('note/create/', views.note_create, name='note_create'),
    path('note/<int:id>/edit/', views.note_update, name='note_update'),
    path('note/<int:id>/delete/', views.note_delete, name='note_delete'),
]
