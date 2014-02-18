from django.shortcuts import render_to_response
from homepage.models import Project
from django.template import RequestContext


def home(request):
    print(request)
    projectLinks = []
    
    # Create project links
    for project in Project.objects.all():
        
        first_item = project.item_set.order_by('-datetime').first()
        
        projectLink = {
            'name': project.name,
            'font_awesome_class': project.font_awesome_class,
            
            # Todo, this url is hardcoded
            'first_item_url': '/items/{0}'.format(first_item.id)
        }
        
        projectLinks.append(projectLink)
        
    
    return render_to_response('home.html',
                              {
                              'projects': Project.objects.all(),
                              'projectLinks': projectLinks
                              },
                              context_instance=RequestContext(request))
