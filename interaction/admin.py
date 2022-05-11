from django.contrib import admin

# Register your models here.
from .models import Teacher, Member, ClassRoom, Checkout

class MemberInline(admin.TabularInline):
    model = Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'class_room', 'teacher']
  
@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['class_room']
    inlines = [MemberInline]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_name']
    inlines = [MemberInline]

@admin.register(Checkout)
class CheckOutAdmin(admin.ModelAdmin):
    list_display = ['checkout_time', 'checkout_choice', 'student_name']