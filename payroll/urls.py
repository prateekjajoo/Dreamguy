from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import TempView, SalaryCreateView, EmployeeSalaryListView, getSalaryDetails, GenerateSalarySlipView
from .views import ProfileView

urlpatterns = [
    path('temp', TempView.as_view(), name='temp'),
    path('salary-create', SalaryCreateView.as_view(), name='salary_create'),
    path('', EmployeeSalaryListView.as_view(), name='emp_salary_list'),
    path('get-emp-salary/<int:emp_id>', getSalaryDetails, name='get_salary_details'),
    path('payslip/<int:emp_id>', GenerateSalarySlipView.as_view(), name='generate_salary_slip'),
    path('profile/<int:emp_id>', ProfileView.as_view(), name='profile_view'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
