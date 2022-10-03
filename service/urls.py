from django.urls import path
from .views import MediaServiceView, MediaServiceDetailView


urlpatterns = [
    path('files/', MediaServiceView.as_view(), name='home'),
    path('files/<uuid:pk>/', MediaServiceDetailView.as_view()),
] 

