from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editor_top', views.editor_top, name='editor_top'),
    path('add_member', views.add_member, name='add_member'),
    path('edit_member/<int:num>', views.edit_member, name='edit_member'),
    path('delete_member/<int:num>', views.delete_member, name='delete_member'),
    path('add_setlist', views.add_setlist, name='add_setlist'),
    path('edit_setlist/<int:num>', views.edit_setlist, name='edit_setlist'),
    path('delete_setlist/<int:num>', views.delete_setlist, name='delete_setlist'),
]
