from django.shortcuts import render
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