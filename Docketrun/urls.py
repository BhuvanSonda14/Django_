from django.urls import path

from . import views

# app_name="Docketrun"
urlpatterns=[
    path('Get_Method/', views.Get_Method, name='Get_Method'),
    path('response/',views.response,name='response'),
    path('get_all_person/',views.get_all_person,name='get_all_person'),
    path('All_employs/',views.All_employs,name="All_employs"),
    path('get_all_person/employ_details/<int:id>/', views.employ_details, name='employ_details'),
    path('All_employs/employ_details/<int:id>/', views.employ_details, name='employ_details'),
    path('main',views.main, name='main'),
    # print(),
    path('main/All_employs/',views.All_employs, name='All_employs'),
    path('testing/',views.testing, name='testing'),
    path('filter/',views.filter, name='filter'),
    path('filter_person/',views.filter_person, name='filter_person'),
    path('filter_person/All_employs/',views.All_employs, name='All_employs'),
    # path('<slug:slug>/', views.slug_view, name='slug_details'),
#  path('post/',views.post, name='post'),
 path('insert_employ/',views.insert_employ, name='insert_employ'),
 path('create_employee/',views.create_employee, name='create_employee'),
 path('get_all_person/delete_employ/<int:id>/', views.delete_employ, name='employ_details'),
 path('delete/<int:id>/', views.delete, name='delete employ'),
 path('get_all_person/update_employ/<int:id>/', views.update_employ, name='update_employ'),
 path('update/<int:id>/', views.update, name='update employ'),
    

]