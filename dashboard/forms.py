from urllib import request
from django import forms
from .models import*
from django.contrib.auth.forms import UserCreationForm

# Notes Form
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

# DateInput
class DateInput(forms.DateInput):
    input_type = 'date'

# Homework Form
class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}
        fields = ['subject','title','description','due','is_finished']

# Youtube Form 
class DashboardForm(forms.Form):
    text = forms.CharField(max_length=255,label="Enter Your Search :")

# Todo Form
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_finished']

# Conversion Form
class ConversionForm(forms.Form):
    CHOICES =[('length','Length'),('mass','Mass')]
    measurement = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)

class ConversionLengthForm(forms.Form):
    CHOICES = [('yard','Yard'),('foot','Foot')]
    input = forms.CharField(required=False,widget=forms.TextInput(
        attrs = {'type':'number','placeholder':'Enter th Number'}
    ))
    measure1 = forms.CharField(
        label='',widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(
        label='',widget = forms.Select(choices = CHOICES)
    )

class ConversionMassForm(forms.Form):
    CHOICES = [('pound','Pound'),('kilogram','Kilogram')]
    input = forms.CharField(required=False,widget=forms.TextInput(
        attrs = {'type':'number','placeholder':'Enter th Number'}
    ))
    measure1 = forms.CharField(
        label='',widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(
        label='',widget = forms.Select(choices = CHOICES)
    )

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
