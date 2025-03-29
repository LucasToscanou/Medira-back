from django.urls import path

from . import views

urlpatterns = [
    path("get_all", views.get_all, name="get_all"),
    path("get_all_ordered/<str:order>/", views.get_all, name="get_all_ordered"),
    path("add_record", views.add_record, name="add_record"),
    path("update_record/<int:record_id>/", views.update_record, name="update_record"),
    path("delete/<int:record_id>/", views.delete_record, name="delete_record"),
]