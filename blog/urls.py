from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.HomepageView.as_view(), name='index'),
    path('new-post/', views.get_new_post, name='new_post'),
    path('edit-post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete-post/', views.delete_post, name='delete_post'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
