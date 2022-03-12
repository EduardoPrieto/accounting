from django.shortcuts import render, redirect
from .forms import CompanyForm
from .models import User_Company, Company

# Create your views here.
def new_company(request):
    if request.user.is_authenticated:
        usuario = request.user
        company_form =CompanyForm()
        if request.method == 'POST':
            data=CompanyForm(request.POST)
            if data.is_valid():
                company = data.save()
                #company.save()
                member = User_Company()
                member.user = usuario
                member.company = company               
                member.save()
                return redirect("/")
        else:
            return render(request, "company/create_company.html", {'form':company_form})
    else:
        return redirect('/login')

def show_company(request):
    if request.user.is_authenticated:
        companys = Company.objects.filter(user=request.user) 
        return render(request, "company/company.html", {'companys':companys})
    # En otro caso redireccionamos al login
    return redirect('/login')

def delete(request, company_id):
    if request.user.is_authenticated:
        companys = Company.objects.filter(id=company_id) 
        companys.delete()
        return redirect('/new_company')
    # En otro caso redireccionamos al login
    return redirect('/login')