from django.forms import ModelForm
from .models import Salary
from django import forms
import pdb

class SalaryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SalaryForm, self).__init__(*args, **kwargs)
        self.visible_fields()[0].field.widget.attrs['class'] = 'select'
        for visible in self.visible_fields()[1:]:
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Salary
        exclude = []
