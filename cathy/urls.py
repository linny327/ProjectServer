from django.urls import path

from cathy import views

urlpatterns = [
    path('add_cattle/', views.add_cattle, name='add_cattle'),
    path('add_user/', views.add_user, name='add_user'),
    path('cattle/', views.cattle, name='cattle'),
    path('chart/', views.chart, name='chart'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('disease/', views.disease, name='disease'),
    path('farm/', views.farm, name='farm'),
    path('monitor/', views.monitor, name='monitor'),
    path('notification/', views.notification, name='notification'),
    path('predict_diagnose/', views.predict_diagnose, name='predict_diagnose'),
    path('profile/', views.profile, name='profile'),
    path('user/', views.user, name='user'),
    path('view_cattle/<int:id>', views.view_cattle, name='view_cattle'),
    path('view_user/<int:id>', views.view_user, name='view_user'),

]
