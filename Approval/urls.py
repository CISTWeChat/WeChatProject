from django.urls import path
from . import views

app_name = 'Approval'
urlpatterns = [
    path('getTemplate/',views.getTemplate),
    path('submitTemplate/',views.submitTemplate),
    # path('approvalTest/<templateId>',views.approvalTest),
    path('showTemplateID/',views.showTemplateID),
    path('addTemplateID/',views.addTemplateID),
    path('saveTemplateID/',views.saveTemplateID),
    path('getUserId/', views.getUserId),


    path('show/<templateId>',views.approvalTest, name="show"),
    
]
