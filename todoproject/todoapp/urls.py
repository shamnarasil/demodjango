from django.urls import path

from todoapp import views

urlpatterns = [

    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.taskListView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.taskDetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.taskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.taskDeleteView.as_view(),name='cbvdelete'),
]
