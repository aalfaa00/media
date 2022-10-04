from django.urls import path, re_path
from .views import MediaServiceView, MediaServiceDetailView


urlpatterns = [
    re_path(r'^files/?', MediaServiceView.as_view(), name='home'),
    path('files/<uuid:pk>', MediaServiceDetailView.as_view()),
    # path('filess/', MediaServiceDetailPutView.as_view())

] 

