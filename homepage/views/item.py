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
        
        context['project_name'] = project.name
        
        context['previous_items'] = Item.objects.order_by('date').filter(project=project).filter(date__lt=self.get_object().date)
            
        context['next_items'] = Item.objects.order_by('date').filter(project=project).filter(date__gt=self.get_object().date)
        
        context['all_items'] = Item.objects.order_by('date').filter(project=project)
            
        projectLinks = []
        
        for project in Project.objects.all():
        
            first_item = project.item_set.order_by('-date').first()
        
            projectLink = {
                'name': project.name,
                'font_awesome_class': project.font_awesome_class,
                
                # Todo, this url is hardcoded
                'first_item_url': '/items/{0}'.format(first_item.id)
            }

            projectLinks.append(projectLink)

        context['projectLinks'] = projectLinks
        
        return context
