from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','demo_link','featured_image','source_link','tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
        # self.fields['demo_link'].widget.attrs.update({'class':'input','placeholder':'Demo Link'})

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})