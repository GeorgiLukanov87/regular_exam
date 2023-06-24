from django.shortcuts import render, redirect

from regular_exam.my_web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, FruitCreateForm, \
    FruitEditForm, FruitDeleteForm
from regular_exam.my_web.models import Fruit, Profile


def get_profile():
    return Profile.objects.first()


def get_fruit(pk):
    return Fruit.objects.filter(pk=pk).get()


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    context = {'fruits': fruits, }
    return render(request, 'common/dashboard.html', context, )


# FRUIT VIEWS:
def create_fruit(request):
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, }

    return render(request, 'fruit/create-fruit.html', context, )


def details_fruit(request, pk):
    fruit = get_fruit(pk)
    context = {'fruit': fruit, }
    return render(request, 'fruit/details-fruit.html', context, )


def edit_fruit(request, pk):
    fruit = get_fruit(pk)

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'fruit': fruit, }

    return render(request, 'fruit/edit-fruit.html', context)


def delete_fruit(request, pk):
    fruit = get_fruit(pk)

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'fruit': fruit, }

    return render(request, 'fruit/delete-fruit.html', context, )


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
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {'form': form, }
    return render(request, 'profile/edit-profile.html', context, )


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, }
    return render(request, 'profile/delete-profile.html', context)


def details_profile(request):
    profile = get_profile()
    fruits = Fruit.objects.all()

    context = {'profile': profile, 'fruits': fruits, }
    return render(request, 'profile/details-profile.html', context, )
