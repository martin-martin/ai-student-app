from lib2to3.refactor import get_all_fix_names
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from interaction.models import Teacher, Member, ClassRoom, Checkout
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'interaction/index.html')

def classroom_list(request):
    class_room_list = ClassRoom.objects.all()
    context = {'class_room_list': class_room_list}
    return render(request, 'interaction/classroom_list.html', context=context)

def student_list(request, classroom_pk):
    classroom = get_object_or_404(ClassRoom, pk=classroom_pk)
    
    context = {'classroom': classroom}
    return render(request, 'interaction/student_list.html', context=context)

def checkout(request, student_pk):
    return HttpResponse("This is checkout page. student pk %s." % student_pk)
