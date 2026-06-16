from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_view, name='login'),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
    
     path(
    'students/',
    views.student_list,
    name='student_list'
),

path(
    'students/add/',
    views.student_add,
    name='student_add'
),
path('students/edit/<int:id>/', views.student_edit, name='student_edit'),
path('students/delete/<int:id>/', views.student_delete, name='student_delete'),


path('attendance/mark/', views.mark_attendance, name='mark_attendance'),

path(
    'attendance/history/',
    views.attendance_history,
    name='attendance_history'
),


path(
    'reports/daily/',
    views.daily_report,
    name='daily_report'
),


path(
    'reports/weekly/',
    views.weekly_report,
    name='weekly_report'
),

path(
    'reports/monthly/',
    views.monthly_report,
    name='monthly_report'
),

path(
    'reports/daily/export/',
    views.export_daily_excel,
    name='export_daily_excel'
),

path('reports/weekly/export/', views.export_weekly_excel, name='export_weekly_excel'),

path('reports/monthly/export/', views.export_monthly_excel, name='export_monthly_excel'),

]

