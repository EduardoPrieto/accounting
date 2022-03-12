from django.urls import path

from . import views

urlpatterns = [
    path('new_company', views.new_company, name='new_company'),
    path('company', views.show_company, name='company'),
    path('delete/<int:company_id>', views.delete, name='delete'),
    
]