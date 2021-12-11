from django.urls import path
from jobsummary import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path("", views.user_login, name="login" ),
   path("dashboard/", views.dashboard, name="dashboard" ),
   path("logout/", views.user_logout, name="logout"),
   path("job_summary/KLGBmeeting", views.KLGBmeeting, name="KLGBcuochop"),
   path("job_summary/KLGBoperation", views.KLGBoperation, name="KLGBvanhanh"),
   path("job_summary/KLGBinvestment", views.KLGBinvestment, name="KLGB_DTXD_SCL"),
   path("job_summary/KLGBother", views.KLGBother, name="KLGBKhac"),
   path("job_summary/createjobsummary", views.createjobsummary, name="Tao_KLGB"),
   path("users/create_user", views.Createuser,name="Create_user"),
   path("users/list_user", views.Listuser, name= "List_user"),
   path("rooms/create_room", views.Create_room, name="Create_room"),
   path("rooms/list_room", views.Listroom, name="List_room"),
   path("job_summary/listjobsummary", views.listjobsummary, name="Danh_sach_KLGB"),
   path("job_summary/editjobsummary/<int:pk>", views.editjobsummary, name="editjobsummary"),
   path("job_summary/listjobsummary/<int:pk>", views.detelejobsummary, name="Danh_sach_KLGB"),
   path("rooms/edit_room/<int:pk>", views.Editroom, name="Edit_room"),
   path("users/edit_user/<int:pk>", views.Edituser, name="Edit_user"),
   path("rooms/delete_room/<int:pk>", views.Deleteroom, name="Delete_room"),
   path("users/delete_user/<int:pk>", views.Deleteuser, name="Delete_user"),
   path("job_summary/assignuser/<int:pk>", views.Assignuser, name="Assign_user"),
   path("job_summary/receivejob/<int:pk>", views.Receivejob, name="Receive_job")
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





