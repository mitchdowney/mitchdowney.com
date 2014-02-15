from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from homepage.models import Project, Item
from homepage.views.project import ProjectListView, ProjectDetailView
from homepage.views.item import ItemListView, ItemDetailView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homepage.views.home', name='home'),
    # url(r'^homepage/', include('homepage.foo.urls')),

    # SHOW HOME PAGE
    url(r'^$', 'homepage.views.home.home', name='home'),

    # SHOW PROJECT
    url(r'^projects/(?P<pk>\d+)/$', ProjectDetailView.as_view(
        model=Project,
        template_name="project_detail.html",
        )),

    # SHOW ITEM
    url(r'^items/(?P<pk>\d+)/$', ItemDetailView.as_view(
        model=Item,
        template_name="item_detail.html",
        ),
        name="item_detail"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)