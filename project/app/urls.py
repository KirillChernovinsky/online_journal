from django.urls import path

from .views import index, create_student, delete, create_object, update

urlpatterns = [
    path('', index, name='home'),
    path('create_student/',create_student, name='create_student'),
    path('delete/<int:id>',delete, name='delete'),
    path('create_object/', create_object, name="create_object"),
    path('update/<int:id>', update, name='update'),
]