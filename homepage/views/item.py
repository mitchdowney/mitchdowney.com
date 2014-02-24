from homepage.models import Item, Project
from django.views.generic import ListView, DetailView

from homepage.utils import group_items_by_dates


class ItemListView(ListView):
    model = Item
    
class ItemDetailView(DetailView):
    model = Item
    context_object_name = "item"
    
    def get_context_data(self, **kwargs):
        
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        project = self.get_object().project
        
        context['current_item'] = self.get_object()
        
        context['project_name'] = project.name
        
        context['previous_items'] = Item.objects.order_by('datetime').filter(project=project).filter(datetime__lt=self.get_object().datetime)
            
        context['next_items'] = Item.objects.order_by('datetime').filter(project=project).filter(datetime__gt=self.get_object().datetime)
        
        context['all_items'] = Item.objects.order_by('datetime').filter(project=project)
            
        projectLinks = []
        
        # Create project links
        for project in Project.objects.all():
            
            first_item = project.item_set.order_by('-datetime').first()
            
            projectLink = {
                'name': project.name,
                'about': project.about,
                'license': project.license,
                'license_link': project.license_link,
                'font_awesome_class': project.font_awesome_class,
                'id': project.id,
                
                # Todo, this url is hardcoded
                'first_item_url': '/items/{0}'.format(first_item.id)
            }
            
            projectLinks.append(projectLink)

        context['projectLinks'] = projectLinks
        
        return context
