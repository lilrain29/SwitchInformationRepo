from django.contrib import admin
from django.urls import path
from switchinfo import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('switch/<int:pk>/', views.switch_detail, name="switch_detail"),
    path('port/update/<int:pk>/', views.update_port, name="update_port"),
    path("update_ports/", views.update_ports, name="update_ports"),
    path("switch/<int:switch_id>/export/", views.export_switch_to_excel, name="export_switch_excel"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
