from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from SMS.models import Course, Customuser, Session_Year, Student 
from django.contrib import messages
from SMS.models import Student

@login_required(login_url='/')
def principal_home(request):
    return render(request, 'principal/principal_home.html')

@login_required(login_url='/')
def add_student(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if Customuser.objects.filter(email=email).exists():
           messages.warning(request,'Email Is Already Taken')
           return redirect('add_student')
        if Customuser.objects.filter(username=username).exists():
           messages.warning(request,'Username Is Already Taken')
           return redirect('add_student')
        else:
            user = Customuser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + " student are Successfully Added !")
            return redirect('add_student')

    context = {
        'course':course,
        'session_year':session_year,
    }
    return render(request,'principal/add_student.html', context)

@login_required(login_url='/')
def view_student(request):
    return render(request,'principal/view_student.html')

@login_required(login_url='/')
def view_student(request):
    student = Student.objects.all()

    context = {
        'student':student,
    }
    return render(request,'principal/view_student.html',context)

@login_required(login_url='/')
def edit_student(request,id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'student':student,
        'course':course,
        'session_year':session_year,
    }
    return render(request,'principal/edit_student.html',context)


@login_required(login_url='/')
def update_student(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        print(student_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = Customuser.objects.get(id = student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id = course_id)
        student.course_id = course

        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request,'Student Record Are Successfully Updated !')
        return redirect('view_student')

    return render(request,'principal/edit_student.html')
#34 update student (Backend).txt
 #34 update student (Backend).txt.

@login_required(login_url='/')
def delete_student(request,admin):
    student = Customuser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record Are Successfully Deleted !')
    return redirect('view_student')


@login_required(login_url='/')
def add_course(request):

    if request.method == "POST":
        course_name = request.POST.get('course_name')

        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request,'Course Are Successfully Created ')

        
        return redirect('view_course')

    return render(request,'principal/add_course.html')