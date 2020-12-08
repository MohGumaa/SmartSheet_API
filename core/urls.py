from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('sheets/<str:id>/', views.view_sheet, name="sheet"),
]
