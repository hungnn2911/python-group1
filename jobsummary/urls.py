from django.urls import path
from jobsummary import views

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
   path("users/list_user", views.Listuser, name= "List_user")


]



