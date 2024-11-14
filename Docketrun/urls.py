from django.urls import path

from . import views

# app_name="Docketrun"
urlpatterns=[
    
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
    path('<slug:slug>/', views.slug_view, name='slug_details'),

]