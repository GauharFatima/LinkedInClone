from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm, EducationForm, SkillForm, ExperienceForm
from .models import Profile
from AccountsApp.models import MyUser
from AccountsApp import urls


def profile_detail(request, user_id):
    my_user = get_object_or_404(MyUser, id=user_id)
    profile = my_user.profile
    return render(request, 'ProfileApp/detail.html', {'my_user': my_user, 'profile': profile})


# following needs some improvements

def profile_test(request):
    return render(request, 'ProfileApp/testing.html', {})


def complete_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.session.get('myuser_id'))

    if request.method == 'POST':
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile)
        education_form = EducationForm(request.POST, prefix='education')
        skill_form = SkillForm(request.POST, prefix='skill')
        experience_form = ExperienceForm(request.POST, prefix='experience')

        forms_are_valid = (profile_form.is_valid() and education_form.is_valid() and
                           skill_form.is_valid() and experience_form.is_valid())

        if forms_are_valid:
            profile_form.save()

            # Save Education, link it to the profile
            education = education_form.save(commit=False)
            education.profile = profile
            education.save()

            # Similar saving process for Skill and Experience
            skill = skill_form.save(commit=False)
            skill.profile = profile
            skill.save()

            experience = experience_form.save(commit=False)
            experience.profile = profile
            experience.save()

            # redirect
            return redirect('profile_detail', user_id=request.MyUser.id)
    else:
        profile_form = ProfileForm(instance=profile)
        education_form = EducationForm(prefix='education')
        skill_form = SkillForm(prefix='skill')
        experience_form = ExperienceForm(prefix='experience')

    context = {
        'profile_form': profile_form,
        'education_form': education_form,
        'skill_form': skill_form,
        'experience_form': experience_form,
    }

    return render(request, 'ProfileApp/complete_profile.html', context)


# def profile_edit(request):
#     profile, created = Profile.objects.get_or_create(user=request.MyUser)

#     if request.method == 'POST':
#         profile_form = ProfileForm(
#             request.POST, request.FILES, instance=profile)
#         education_formset = EducationFormSet(request.POST, instance=profile)
#         skill_formset = SkillFormSet(request.POST, instance=profile)
#         experience_formset = ExperienceFormSet(request.POST, instance=profile)

#         if (profile_form.is_valid() and education_formset.is_valid() and
#                 skill_formset.is_valid() and experience_formset.is_valid()):
#             profile_form.save()
#             education_formset.save()
#             skill_formset.save()
#             experience_formset.save()
#             # Redirect to the profile detail view or another appropriate view
#             return redirect('feeds')

#     else:
#         profile_form = ProfileForm(instance=profile)
#         education_formset = EducationFormSet(instance=profile)
#         skill_formset = SkillFormSet(instance=profile)
#         experience_formset = ExperienceFormSet(instance=profile)

#     return render(request, 'ProfileApp/edit.html', {
#         'profile_form': profile_form,
#         'education_formset': education_formset,
#         'skill_formset': skill_formset,
#         'experience_formset': experience_formset,
#     })
