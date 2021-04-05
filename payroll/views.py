from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView, View
from .models import Salary, Employee
from .forms import SalaryForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
import pdb

# Create your views here.
class TempView(TemplateView):
    template_name = "temp.html"


class EmployeeSalaryListView(ListView):
    model = Employee
    template_name = 'salary.html'

    def get(self, request, *args, **kwargs):
        emp_list = Employee.objects.all()
        id_list = list(set([i.id  for i in Employee.objects.all()]) - set([i.employee.id  for i in Salary.objects.all()]))
        sec_list = Employee.objects.filter(id__in = id_list)
        return render(request, "salary.html", {'employee_list': emp_list, 'sec_employee_list': sec_list})


class SalaryCreateView(CreateView):
    model = Salary
    form_class = SalaryForm
    template_name = 'temp.html'

    # def get(self, request, *args, **kwargs):
    #     # pdb.set_trace()
    #     kwargs['emp_list'] = Employee.objects.all()
    #     return super(SalaryCreateView, self).get(self, request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        employee = Employee.objects.get(id=request.POST['staff'])
        basic = float(request.POST['basic'])
        DA = float(request.POST['da'])
        HRA = float(request.POST['hra'])
        Conveyance = float(request.POST['conveyance'])
        Allowance = float(request.POST['allowance'])
        Medical_Allowance = float(request.POST['medical_allowance'])
        other_earnings = float(request.POST['other_earnings'])
        TDS = float(request.POST['tds'])
        ESI = float(request.POST['esi'])
        PF = float(request.POST['pf'])
        Leave = float(request.POST['leave'])
        Prof_Tax = float(request.POST['prof_tax'])
        Labour_Welfare = float(request.POST['labour_welfare'])
        other_deductions = float(request.POST['other_deductions'])
        net_salary = float(request.POST['net_salary'])

        if Salary.objects.filter(employee=employee):
            salary_obj = Salary.objects.filter(employee=employee).latest('id')
            sal_obj = Salary(id = salary_obj.id, employee=employee, basic=basic, DA=DA, HRA=HRA, Conveyance=Conveyance, Allowance=Allowance,
                             Medical_Allowance=Medical_Allowance,
                             other_earnings=other_earnings, TDS=TDS, ESI=ESI, PF=PF, Leave=Leave, Prof_Tax=Prof_Tax,
                             Labour_Welfare=Labour_Welfare, other_deductions=other_deductions, net_salary=net_salary)
        else:
            sal_obj = Salary(employee=employee, basic= basic, DA=DA, HRA=HRA, Conveyance=Conveyance, Allowance= Allowance, Medical_Allowance= Medical_Allowance,
               other_earnings = other_earnings, TDS = TDS, ESI=ESI, PF=PF, Leave=Leave, Prof_Tax=Prof_Tax, Labour_Welfare= Labour_Welfare
               , other_deductions = other_deductions, net_salary = net_salary)

        Salary.save(sal_obj)
        return redirect("emp_salary_list")



class GenerateSalarySlipView(TemplateView):

    def get(self, request, *args, **kwargs):
        salary_obj = []
        if Salary.objects.filter(employee=self.kwargs['emp_id']):
            salary_obj = Salary.objects.filter(employee=self.kwargs['emp_id']).latest('id')
        return render(request, "salary-view.html", {'emp_obj': Employee.objects.get(pk=self.kwargs['emp_id']), 'sal_obj' : salary_obj})


def getSalaryDetails(request, emp_id):

    if Salary.objects.filter(employee=emp_id):
        salary_obj = Salary.objects.filter(employee=emp_id).latest('id')
        return HttpResponse(serializers.serialize("json", [Employee.objects.get(pk=emp_id), salary_obj]))
    return HttpResponse(serializers.serialize("json", [Employee.objects.get(pk=emp_id)]))


class ProfileView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, "profile.html", {'emp_obj': Employee.objects.get(pk=self.kwargs['emp_id'])})
