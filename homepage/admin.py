from django.contrib import admin
from homepage.models import Project, Item, Tool, Type

for model in [Project, Item, Tool, Type]:
    admin.site.register(model)