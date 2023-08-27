from django.urls import path, include
from .views import Description, Title, Duedate, Status

urlpatterns = [
    path('description/', Description.as_view()),
    path('title/', Title.as_view()),
    path('duedate/', Duedate.as_view()),
    path('status/', Status.as_view())
]
