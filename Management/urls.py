from django.urls import path
from . import views

app_name = 'Management'
urlpatterns = [
    path('login/',views.login,name="login"),
    path('loginRes/',views.loginRes,name="loginRes"),
    path('logout/',views.logout,name="logout"),

    path('showApproval/',views.showApproval,name="showExam"),
    path('showInfo/',views.showInfo,name="showInfo"),

    path('',views.index,name="index"),
]