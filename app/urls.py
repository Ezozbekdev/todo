from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import MainView, MainDetail, MainEdit, DeleteMain, CreateMain, LoginPage, Register

urlpatterns = [
    path('', MainView.as_view(), name="main"),
    path('detail/<int:pk>/', MainDetail.as_view(), name="detail"),
    path('edit/<int:pk>/', MainEdit.as_view(), name="edit"),
    path('delete/<int:pk>/', DeleteMain.as_view(), name="delete"),
    path('create/', CreateMain.as_view(), name='create'),
    path('accounts/login/', LoginPage.as_view(), name='login'),
    path('log-out/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register')
]