from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='dashboard-profile'),
    path('notice/', views.notice, name='dashboard-notice'),
    path('notice-add/', views.notice_add, name='dashboard-notice-add'),
    path('notice-edit/<int:id>', views.notice_edit, name='dashboard-notice-edit'),
    path('notice-remove/<int:id>', views.notice_remove, name='dashboard-notice-remove'),
]