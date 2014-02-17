from django.contrib import admin
from homepage.models import Project, Tool, Type, Item

for model in [Project, Tool, Type, Item]:
    admin.site.register(model)