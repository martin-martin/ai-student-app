from lib2to3.refactor import get_all_fix_names

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from interaction.models import Checkout, ClassRoom, Member, Teacher

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

def checkout(request):
    if request.method == "POST":
        # print(request.POST)
        student_id = request.POST["student"]
        return HttpResponse(f"This is checkout page. student pk {student_id}")
    else:
        return HttpResponse(f"This is an empty checkout page.")
