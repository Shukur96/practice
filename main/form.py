from django import forms
from . models import Employee,Product,Mentor,Group,Student
from django.contrib.auth.models import User
from  django.contrib.auth.forms import UserCreationForm

class CreateUserForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name','birth_date','country','city','adress','salari']
        
class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','model','release_date','made_in','coment','price',]
        
class CreateMentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['full_name','cpetification','gender','birth_date','country','city','adress','salari',]
        
class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'cpetification','gender','birth_date','country','adress']
        
class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'cpetification', 'mentor', 'leson_qty', 'student_qty', 'price', 'time', 'room']