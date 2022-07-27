from django.urls import path
from . import views

urlpatterns = [
    
    path('registr/',views.RegisterApiView.as_view(),name='registr')
]