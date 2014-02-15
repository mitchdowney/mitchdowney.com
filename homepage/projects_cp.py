from homepage.models import Project

def projects_list(request):
    
    return {
        'projects': Project.objects.all()
    }
