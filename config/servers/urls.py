from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("servers/", views.server_list, name="server_list"),
    path("servers/create/", views.server_create, name="server_create"),
    path("servers/<int:pk>/update/", views.server_update, name="server_update"),
    path("servers/<int:pk>/delete/", views.server_delete, name="server_delete"),    
    path("servers/<int:pk>/detail/", views.server_detail, name="server_detail"),

]

