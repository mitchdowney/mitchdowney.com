from django.db import models
from django.core.urlresolvers import reverse
from time import time

def get_upload_file_name(instance, filename):
    return "%s_%s" % (str(time()).replace('.', '_'), filename)

class Project(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    
    font_awesome_class = models.CharField(max_length=50)
    
    def __unicode__(self):
        return u'%s' % (self.name)
        
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': str(self.id)})

class Item(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to=get_upload_file_name)
    
    def __unicode__(self):
        return u'%s' % (self.name)
        
    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'pk': str(self.id)})
        
    def get_grouped_items(self, project):
        
        this.objects.all()
        """
        grouped_item_collection = {}
    
        def date(item):
            #print item.date.strftime('%B %Y')
            return item.date.strftime('%B %Y')
            
        gb = itertools.groupby(items, date)
        
        for group, items in gb:
            grouped_item_collection[group] = list(items)
        """
