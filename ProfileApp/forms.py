from django import forms
from django.forms.models import inlineformset_factory
from .models import Profile, Education, Experience, Skill


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree',
                  'start_year', 'end_year', 'description']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['employment_type', 'company_name', 'title', 'location',
                  'location_type', 'start_date', 'end_date', 'description']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name']


EducationFormSet = inlineformset_factory(
    Profile, Education,
    form=EducationForm,
    extra=1,
    can_delete=True
)

SkillFormSet = inlineformset_factory(
    Profile, Skill,
    form=SkillForm,
    extra=1,
    can_delete=True
)

ExperienceFormSet = inlineformset_factory(
    Profile, Experience,
    form=ExperienceForm,
    extra=1,
    can_delete=True
)

