from .views import CenterListDetailUpdateDeleteAPIView,CenterReviewDetailUpdateDeleteAPIView,CenterList,CenterDetailView
from django.urls import path

app_name = 'centers'


urlpatterns = [
    path('center', CenterListDetailUpdateDeleteAPIView.as_view()),
    path('center/<int:pk>/', CenterReviewDetailUpdateDeleteAPIView.as_view()),

    path('',CenterList.as_view(), name='center-list'),
    path('<int:pk>/center-detail/', CenterDetailView.as_view(), name='center-detail'),

]
