from django.forms import ModelForm
from .models import Profile,Skill
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#Profile = apps.get_model('users','Profile')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels = {
            'first_name':'Name'
        }

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
        # self.fields['demo_link'].widget.attrs.update({'class':'input','placeholder':'Demo Link'})

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','username','location','bio','short_intro','profile_image',
                    'social_github','social_twitter','social_website']
    
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
        # self.fields['demo_link'].widget.attrs.update({'class':'input','placeholder':'Demo Link'})

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
        # self.fields['demo_link'].widget.attrs.update({'class':'input','placeholder':'Demo Link'})

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})