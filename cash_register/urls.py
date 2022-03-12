from django.urls import path

from . import views

urlpatterns = [
    path('new_expense', views.new_expense, name='new_expense'),
    path('expenses/<int:company_id>', views.show_expenses, name='expenses'),
    path('new_sale', views.new_sale, name='new_sale'),
    path('sales/<int:company_id>', views.show_sales, name='sales'),

    
]