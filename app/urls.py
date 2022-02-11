from django.urls import path
from .views import index_view,delete_task, edit_view
urlpatterns=[
    path('', index_view, name='home_page'),
    path('task/<int:id>/edit/', edit_view, name='edit_task'),
    path('task/<int:id>/delete/', delete_task, name='delete_task'),
]