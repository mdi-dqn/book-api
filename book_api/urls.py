from django.urls import path
from . import views

app_name = 'book_api'

urlpatterns = [
    path('books/', views.BookView.as_view()),
    path('books/<int:pk>/', views.BookView.as_view()),
]
