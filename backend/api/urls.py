from django.urls import path
from .views import Jobview,JobListView, PlaceView, PlaceListView, JobnamesListView, JobnamesCreateView, JobDetailView

urlpatterns = [
    path('jobs', JobListView.as_view()),
    path('add-jobs', Jobview.as_view()),
    path('places',PlaceListView.as_view()),
    path('create',PlaceView.as_view()),
    path('jobnames', JobnamesListView.as_view()),
    path('createjobnames',JobnamesCreateView.as_view()),
    path('<pk>',JobDetailView.as_view())

]
