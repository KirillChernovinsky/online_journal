from django.shortcuts import render, redirect

from .forms import StudentForm, ObjectForm
from .models import Student, Object, Estimation


# Create your views here.


def index(request):
    student = Student.objects.all()
    print(student)
    return render(request, "index.html", context={'student':student})



def create_student(request):
    marks = Estimation.objects.all()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            object = form.cleaned_data['object']
            estimation = request.POST.get('estimation')
            average_score = form.cleaned_data['average_score']
            student, _ = Student.objects.get_or_create(name=name,
                                                   surname=surname,
                                                   object_id=object,
                                                   estimation_id=estimation,
                                                       average_score=average_score)
            return redirect('home')
        else:
            form = StudentForm()
            return render(request, 'create_student.html', context={'form': form})
    else:
        form = StudentForm()
        return render(request, 'create_student.html', context={'form': form, 'marks': marks})


def update(request, id):
    try:
        men = Student.objects.get(id=id)
        if request.method == "POST":
            men.name = request.POST.get('name')
            men.surname = request.POST.get('surname')
            men.object.name = request.POST.get('object')
            men.object.save()
            men.estimation.estimation = request.POST.get('estimation')
            men.estimation.save()
            men.save()
            return redirect('home')
        else:
            return render(request, 'update.html', context={'men': men, 'marks': Estimation.objects.all()})
    except Exception as e:
        print(e)
        return redirect('create_student')














def create_object(request):
    if request.method == "POST":
        form = ObjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            objects, _ = Object.objects.get_or_create(name=name)
            return redirect('home')
        else:
            form = ObjectForm()
            return render(request, 'create_objects.html', context={'form': form})
    else:
        form = ObjectForm()
        return render(request, 'create_objects.html', context={'form': form})




def delete(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return redirect('home')
    except:
        pass


