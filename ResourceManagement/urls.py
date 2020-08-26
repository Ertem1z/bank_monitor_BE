from ResourceManagement import views
from django.urls import path

urlpatterns = [
    path('resourceBrowse/', views.getResourceList),
    path('resourceBrowse/add/', views.addResource),
    path('resourceBrowse/edit/', views.editResource),
    path('resourceBrowse/addmonitor/', views.AddResourceById),
    path('resourceBrowse/delmonitor/', views.delResourceById),
    path('resourceBrowse/remove/', views.removeResourceById),
]