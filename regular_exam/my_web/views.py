from django.shortcuts import render, redirect

from regular_exam.my_web.forms import ProfileCreateForm
from regular_exam.my_web.models import Fruit, Profile


def get_profile():
    return Profile.objects.first()


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    context = {'fruits': fruits, }
    return render(request, 'common/dashboard.html', context, )


# FRUIT VIEWS:
def create_fruit(request):
    return render(request, 'fruit/create-fruit.html')


def details_fruit(request, pk):
    return render(request, 'fruit/details-fruit.html')


def edit_fruit(request, pk):
    return render(request, 'fruit/edit-fruit.html')


def delete_fruit(request, pk):
    return render(request, 'fruit/delete-fruit.html')


# PROFILE VIEWS:
def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, }

    return render(request, 'profile/create-profile.html', context, )


def edit_profile(request):
    return render(request, 'profile/edit-profile.html')


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')


def details_profile(request):
    profile = get_profile()
    fruits = Fruit.objects.all()
    context = {'profile': profile, 'fruits': fruits, }
    return render(request, 'profile/details-profile.html', context, )
