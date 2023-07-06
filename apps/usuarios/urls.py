from django.urls import path

from .apiviews import CreateUserApiView, UpdateUserApiView, DeleteUserApiView, RetrieveUserApiView

urlpatterns = [
    path('register/', CreateUserApiView.as_view()),
    path('view/<int:pk>/', RetrieveUserApiView.as_view()),
    path('update/<int:pk>/', UpdateUserApiView.as_view()),
    path('delete/<int:pk>/', DeleteUserApiView.as_view()),
]