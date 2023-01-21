from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import *
from .models import student
from .models import Signup
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    return render(request, 'home.html',{'name':'Ahmed'})

# Add student form
def addStudent(request):
    # Submit student adding form
    if request.method== 'POST':
        name = request.POST['name']
        nationalId = request.POST['nationalId']
        regno = request.POST['regno']
        course = request.POST['course']
        gender = request.POST['gender']
        mode = request.POST['mode']
        languages = request.POST.getlist('languages')
        # allLangs = len(languages) - getting length of a list
        allLangs = ''
        for lang in languages:
            allLangs += lang+','

        if(student.objects.filter(regno=regno).exists()):
            messages.info(request, 'Registration number already taken.')
            return redirect("add-student")
        elif(student.objects.filter(nationalId=nationalId).exists()):
            messages.info(request, 'National Id already exists.')
            return redirect("add-student")
        else:
            st = student(name=name, nationalId=nationalId, regno=regno, course=course, gender=gender, mode=mode, languages=allLangs) 
            st.save()
            messages.info(request, "Student registered.") 

    # Render HTML form
    context = {
        'form':studentForm
    } 
    return render(request, 'add-student.html', context)


def studentList(request):
    # all_students= student.objects.all().order_by('-id')[:15] 
    all_students= student.objects.all().order_by('-id')   

    context= { 
        'students': all_students
    } 

    return render(request, 'students.html', context)
    
# Delete student
def deleteStudent(request, id):
    obj = get_object_or_404(student, id=id)
    obj.delete()
    messages.info(request, 'Student deleted.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) # Redirect to previous page

# Edit student



def editStudent(request, id):
    obj = get_object_or_404(student, id=id)
    form = studentForm(request.POST or None, instance = obj)

    if form.is_valid:
        form.save()
        return render(request, 'students.html')

    student_to_edit = student.objects.get(id=id)
    languages = student_to_edit.languages
    result = languages.split(",")
    
    context = {
        'form':studentForm(initial={
            'name':student_to_edit.name,
            'nationalId':student_to_edit.nationalId,
            'regno':student_to_edit.regno,
            'course':student_to_edit.course, 
            'mode':student_to_edit.mode,
            }),
        'languages':result,
    } 
    #item = Item.objects.get(id=id) 
    #form = ItemForm(initial={'name': item.name}) 
    #return render_to_response('bounded_form.html', {'form': form}) 

    return render(request, 'edit-student.html', context)


# Sign In
def signIn(request):
    return render(request, 'sign-in.html')


#Sign Up
# def signUp(request):
#     return render(request, 'sign-up.html')
#exams
def exams(request):
    return render(request, 'exams.html')



#  student Sign up form
def signUp(request):
    # Submit student 
    if request.method== 'POST':
        studentname = request.POST['studentname']
        regno = request.POST['regno']



        #yessssssssssssssssssssss
        if(Signup.objects.filter(regno=regno).exists()):
            messages.info(request, 'Registration number already taken.')
            return redirect("sign-up")
      
        else:
            st = Signup(studentname=studentname, regno=regno) 
            st.save()
            messages.info(request, "Signup registered.") 

    # Render HTML form
    context = {
        'form':studentSignup
    } 
    return render(request, 'sign-up.html', context)




        
      


      