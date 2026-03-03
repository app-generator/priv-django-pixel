from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project


@login_required(login_url="/login/")
def project_list(request):
    """Widok listy projektów przypisanych do użytkownika."""
    projects = Project.objects.filter(user=request.user)
    context = {
        'projects': projects,
        'segment': 'projects',
    }
    return render(request, 'projects/projects_list.html', context)