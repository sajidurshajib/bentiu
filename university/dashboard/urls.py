from django.urls import path
from . import views
from notices.views import notice, notice_add, notice_edit, notice_remove

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='dashboard-profile'),
    path('notice/', notice, name='dashboard-notice'),
    path('notice-add/', notice_add, name='dashboard-notice-add'),
    path('notice-edit/<int:id>', notice_edit, name='dashboard-notice-edit'),
    path('notice-remove/<int:id>', notice_remove, name='dashboard-notice-remove'),
]