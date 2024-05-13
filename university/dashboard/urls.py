from django.urls import path
from . import views
from notices.views import notice, notice_add, notice_edit, notice_remove
from news.views import news, news_add, news_remove, news_edit

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='dashboard-profile'),
    path('notice/', notice, name='dashboard-notice'),
    path('notice-add/', notice_add, name='dashboard-notice-add'),
    path('notice-edit/<int:id>', notice_edit, name='dashboard-notice-edit'),
    path('notice-remove/<int:id>', notice_remove, name='dashboard-notice-remove'),
    path('news/', news, name='dashboard-news'),
    path('news-add/', news_add, name='dashboard-news-add'),
    path('news-edit/<int:id>', news_edit, name='dashboard-news-edit'),
    path('news-remove/<int:id>', news_remove, name='dashboard-news-remove'),

]