from .views import CenterListDetailUpdateDeleteAPIView,CenterReviewDetailUpdateDeleteAPIView,CenterList,CenterDetailView
from django.urls import path

app_name = 'centers'


urlpatterns = [
    path('api', CenterListDetailUpdateDeleteAPIView.as_view()),
    path('api/<int:pk>/', CenterReviewDetailUpdateDeleteAPIView.as_view()),

    path('',CenterList.as_view(), name='center-list'),
    path('<int:pk>/center-detail/', CenterDetailView.as_view(), name='center-detail'),

]
