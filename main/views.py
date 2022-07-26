from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import *
from . form import  *
# Create your views here.
def registerUser(request):
    form = CreateUserForms()
    if request.method == "POST":
        form = CreateUserForms(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request,'mainapp/register.html',context)

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,"Username or password was incorrect")
            
    context = {
        
    }
    return render(request, 'mainapp/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login_user')

@login_required(login_url='login_user')
def dashboard(request):
    return render(request,'mainapp/dashboard.html')
    
    
def testPage(request):
    return render(request,'mainapp/base.html')

def dashboardPage(request):
    return render(request,'mainapp/dashboard.html')

def tablePage(request):
    employees = Employee.objects.all()
    
    context = {
        'employees' : employees
    }
    return render(request,'mainapp/e-table.html',context)


def createEmployee(request):
    form = CreateEmployeeForm()
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('e-table')
        else:
            form = CreateEmployeeForm()

    context = {
        'form':form
    }
    return render(request,'mainapp/e_create.html',context)

def updateEmployee(request,pk):
    
    employee = Employee.objects.get(id=pk)
    form = CreateEmployeeForm(instance=employee)
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('e-table')
        
    context = {
        'form':form
        }
    return render (request, 'mainapp/e_create.html',context)

def deleteEmployee(request,pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('e-table') 
    
    context = {
        'employee':employee
        }
    return render (request,'mainapp/e_delete.html',context)

def productTable(request):
    products = Product.objects.all()
    
    context = {
        'products':products
    }
    return render(request,'mainapp/p_table.html',context)

def createProduct(request):
    form = CreateProductForm()
    if request.method == "POST":
        form = CreateProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('p_table')
        else:
            form = CreateProductForm()

    context = {
        'form':form
    }
    return render(request,'mainapp/p_create.html',context)

def updateProduct(request,pk):
    
    product = Product.objects.get(id=pk)
    form = CreateProductForm(instance=product)
    if request.method == "POST":
        form = CreateProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('p_table')
        
    context = {
        'form':form
        }
    return render (request, 'mainapp/p_create.html',context)

def deleteproduct(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('e-table') 
    
    context = {
        'product':product
        }
    return render (request,'mainapp/p_delete.html',context)

def mentorTable(request):
    mentors = Mentor.objects.all()
    
    context = {
        'mentors':mentors
    }
    return render(request,'mainapp/m-table.html',context)

def createMentor(request):
    form = CreateMentorForm()
    if request.method == "POST":
        form = CreateMentorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('m-table')
        else:
            form = CreateMentorForm()

    context = {
        'form':form
    }
    return render(request,'mainapp/m_creat.html',context)

def updateMentor(request,pk):
    
    mentor = Mentor.objects.get(id=pk)
    form = CreateMentorForm(instance=mentor)
    if request.method == "POST":
        form = CreateMentorForm(request.POST,instance=mentor)
        if form.is_valid():
            form.save()
            return redirect('m-table')
        
    context = {
        'form':form
        }
    return render (request, 'mainapp/m_creat.html',context)

def deleteMentor(request,pk):
    mentor = Mentor.objects.get(id=pk)
    if request.method == "POST":
        mentor.delete()
        return redirect('m-table') 
    
    context = {
        'mentor':mentor
        }
    return render (request,'mainapp/m_delete.html',context)

def groupTable(request):
    groups = Group.objects.all()
    
    context = {
        'groups':groups
    }
    return render(request,'mainapp/group_teb.html',context)

def createGroup(request):
    form = CreateGroupForm()
    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('group_teb')
        else:
            form = CreateGroupForm()

    context = {
        'form':form
    }
    return render(request,'mainapp/group_crt.html',context)

def updateGroup(request,pk):
    
    group = Group.objects.get(id=pk)
    form = CreateGroupForm(instance=group)
    if request.method == "POST":
        form = CreateGroupForm(request.POST,instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_teb')
        
    context = {
        'form':form
    }
    return render (request, 'mainapp/group_crt.html',context)

def deleteGroup(request,pk):
    group = Group.objects.get(id=pk)
    if request.method == "POST":
        group.delete()
        return redirect('group_teb') 
    
    context = {
        'group':group
        }
    return render (request,'mainapp/group_del.html',context)

def studentTable(request):
    students = Student.objects.all()
    
    context = {
        'students':students
    }
    return render(request,'mainapp/student_teb.html',context)

def createStudent(request):
    form = CreateStudentForm()
    if request.method == "POST":
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('student_teb')
        else:
            form = CreateStudentForm()

    context = {
        'form':form
    }
    return render(request,'mainapp/student_crt.html',context)

def updateStudent(request,pk):
    
    student = Student.objects.get(id=pk)
    form = CreateStudentForm(instance=student)
    if request.method == "POST":
        form = CreateStudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_teb')
        
    context = {
        'form':form
    }
    return render (request, 'mainapp/student_crt.html',context)

def deleteStudent(request,pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_teb') 
    
    context = {
        'student':student
        }
    return render (request,'mainapp/student_del.html',context)

def error_400(request):
    return render (request,'mainapp/error_400.html')
def error_500(request):
    return render (request,'mainapp/error_500.html')