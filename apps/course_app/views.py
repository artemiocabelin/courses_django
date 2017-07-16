from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Course, Description, Comment

# Create your views here.
def index(request):
    course_list = Course.objects.values()
    desc_list   = Description.objects.values()
    course_desc = zip(course_list,desc_list)
    context = {
        'course_desc' : course_desc
    }
    return render(request, 'course_app/index.html', context, messages)

def add(request):
    if request.method == 'POST':
        # add course
        course_name = request.POST['name']
        course_desc = request.POST['desc']
        # validate first
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
        else:
            course1 = Course(name=course_name)
            course1.save()
            description = Description(desc=course_desc, course=course1)
            description.save()

    return redirect('/')

def warning(request,course_id):
    # renders warning page
    course = Course.objects.get(id=course_id)
    descri = Description.objects.get(course_id=course_id)
    context = {
        'course' : course,
        'descri' : descri
    }
    return render(request, 'course_app/warning.html', context)

def delete(request,course_id):
    # delete course
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('/')

def comments(request,course_id):
    comment_list = Comment.objects.filter(course_id=course_id).order_by("-created_at").values()
    context = {
        'course_id' : course_id,
        'comment_list' : comment_list
    }
    return render(request, 'course_app/comments.html', context)

def post(request, course_id):
    if request.method == 'POST':
        course = Course.objects.get(id=course_id)
        comment = Comment(content=request.POST['comment'],course=course)
        comment.save()
    return redirect('/comments/'+course_id)