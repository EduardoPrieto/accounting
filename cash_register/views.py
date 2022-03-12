from django.shortcuts import render, redirect
from .models import Expenses, Sales
from .forms import ExpensesForm, SalesForm
from company.models import Company

# Create your views here.
# Create your views here.
def new_expense(request):
    if request.user.is_authenticated:
        usuario = request.user.username
        expense_form =ExpensesForm()
        expense = Expenses()
        if request.method == 'POST':
            data=ExpensesForm(request.POST)
            if data.is_valid():
                expense = data
                expense.save()
                return redirect("/")
        else:
            return render(request, "cash_register/new_expense.html", {'form':expense_form})
    else:
        return redirect('/login')

def show_expenses(request, company_id):
    if request.user.is_authenticated:
        company = Company.objects.get(id=company_id) 
        expenses = Expenses.objects.filter(company=company) 
        #print(expensess)
        return render(request, "cash_register/expenses.html", {'expenses':expenses})
    # En otro caso redireccionamos al login
    return redirect('/login')


def new_sale(request):
    if request.user.is_authenticated:
        usuario = request.user.username
        sale_form =SalesForm()
        sale = Sales()
        if request.method == 'POST':
            data=SalesForm(request.POST)
            if data.is_valid():
                sale = data
                sale.save()
                return redirect("/")
        else:
            return render(request, "cash_register/new_sale.html", {'form':sale_form})
    else:
        return redirect('/login')

def show_sales(request, company_id):
    if request.user.is_authenticated:
        company = Company.objects.get(id=company_id) 
        sales = Sales.objects.filter(company=company) 
        #print(saless)
        return render(request, "cash_register/sales.html", {'sales':sales})
    # En otro caso redireccionamos al login
    return redirect('/login')