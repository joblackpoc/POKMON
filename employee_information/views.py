from django.shortcuts import redirect, render
from django.http import HttpResponse
from employee_information.models import Department, Position, Employee
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json
employee = [

    {
        'code':1,
        'name':"John D Smith",
        'contact':'09123456789',
        'address':'Sample Address only'
    },{
        'code':2,
        'name':"Claire C Blake",
        'contact':'09456123789',
        'address':'Sample Address2 only'
    }

]
# Login
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')

#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')

# Create your views here.
@login_required
def home(request):
    context = {
        'page_title':'Home',
        'employee':employee,
        'total_department':len(Department.objects.all()),
        'total_position':len(Position.objects.all()),
        'total_employee':len(Employee.objects.all()),
    }
    return render(request, 'employee_information/home.html',context)


def about(request):
    context = {
        'page_title':'About',
    }
    return render(request, 'employee_information/about.html',context)

# Departments
@login_required
def department(request):
    department_list = Department.objects.all()
    context = {
        'page_title':'Department',
        'department':department_list,
    }
    return render(request, 'employee_information/department.html',context)
@login_required
def manage_department(request):
    department = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            department = Department.objects.filter(id=id).first()
    
    context = {
        'department' : department
    }
    return render(request, 'employee_information/manage_department.html',context)

@login_required
def save_department(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_department = Department.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],status = data['status'])
        else:
            save_department = Department(name=data['name'], description = data['description'],status = data['status'])
            save_department.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_department(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Department.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

# Positions
@login_required
def position(request):
    position_list = Position.objects.all()
    context = {
        'page_title':'Position',
        'position':position_list,
    }
    return render(request, 'employee_information/position.html',context)
@login_required
def manage_position(request):
    position = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            position = Position.objects.filter(id=id).first()
    
    context = {
        'position' : position
    }
    return render(request, 'employee_information/manage_position.html',context)

@login_required
def save_position(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_position = Position.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],status = data['status'])
        else:
            save_position = Position(name=data['name'], description = data['description'],status = data['status'])
            save_position.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_position(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Position.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
# Employees
def employee(request):
    employee_list = Employees.objects.all()
    context = {
        'page_title':'Employee',
        'employee':employee_list,
    }
    return render(request, 'employee_information/employee.html',context)
@login_required
def manage_employee(request):
    employee = {}
    department = Department.objects.filter(status = 1).all() 
    position = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'department' : department,
        'position' : position
    }
    return render(request, 'employee_information/manage_employee.html',context)

@login_required
def save_employee(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['fname']) :
        check  = Employee.objects.filter(fname = data['fname'])
    else:
        check  = Employee.objects.filter(lname = data['lname'])

    if len(check) == '':
        resp['status'] = 'failed'
        resp['msg'] = 'ชื่อ นามสกุล ต้องใส่นะ'
    else:
        try:
            dept = Department.objects.filter(id=data['department_id']).first()
            pos = Position.objects.filter(id=data['position_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_employee = Employee.objects.filter(id = data['id']).update( fname = data['fname'],lastname = data['lname'],gender = data['gender'],contact = data['contact'],address = data['address'],department_id = dept,position_id = pos,date_hired = data['date_hired'],status = data['status'])
            else:
                save_employee = Employee(fname = data['fname'],lastname = data['lname'],gender = data['gender'],contact = data['contact'],address = data['address'],department_id = dept,position_id = pos,date_hired = data['date_hired'],status = data['status'])
                save_employee.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"firstname" : data['firstname'],"lastname" : data['lastname'],"gender" : data['gender'],"contact" : data['contact'],"address" : data['address'],"department_id" : data['department_id'],"position_id" : data['position_id'],"date_hired" : data['date_hired'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_employee(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Employees.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_employee(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employee.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
    return render(request, 'employee_information/view_employee.html',context)