from django.contrib import admin
from homepage.models import Project, Item

for model in [Project, Item]:
    admin.site.register(model)