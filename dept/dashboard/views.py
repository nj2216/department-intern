from django.shortcuts import render, redirect
from .models import Department

# Create your views here.
def hom(request):
    depts = Department.objects.all()
    if request.method == "POST":
        dept_id = request.POST.get("dept_id")
        dept_name = request.POST.get("dept_name")
        dept_code = request.POST.get("dept_code")
        dept_head = request.POST.get("dept_head")

        # Create a new department instance
        new_dept = Department(
            dept_id=dept_id,
            dept_name=dept_name,
            dept_code=dept_code,
            dept_head=dept_head
        )
        new_dept.save()
    return render(request, "dashboard/index.html", {"depts": depts})

def edit(request, dept_id):
    dept = Department.objects.get(dept_id=dept_id)
    if request.method == "POST":
        action = request.POST.get('action')
        if action == "delete":
            dept.delete()
            return redirect("home")
        if action == "update":
            dept.dept_id = request.POST.get("dept_id")
            dept.dept_name = request.POST.get("dept_name")
            dept.dept_code = request.POST.get("dept_code")
            dept.dept_head = request.POST.get("dept_head")
            dept.save()
            return redirect("home")
    return render(request, "dashboard/edit.html", {"dept": dept})
