from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.HomepageView.as_view(), name='index'),
    path('new-post/', views.get_new_post, name='new_post'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]