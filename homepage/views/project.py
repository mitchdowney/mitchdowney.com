from homepage.models import Project, Item
from django.views.generic import ListView, DetailView

class ProjectListView(ListView):
    model = Project
    
class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"