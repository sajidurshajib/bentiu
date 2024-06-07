from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('about/vc', views.vc, name='about-vc'),
    path('schools/', views.schools, name='schools'),
    path('schools/<str:slug>', views.schools_detail, name='school-detail'),
    path('courses/<str:slug>', views.course_detail, name='course-detail'),
    path('notices/', views.notice, name='notices'),
    path('notices/<str:slug>', views.notice_detail, name='notice-detail'),
    path('news/', views.news, name='news'),
    path('news/<str:slug>', views.news_detail, name='news-detail'),
    path('contact/', views.contacts, name='contact'),
]