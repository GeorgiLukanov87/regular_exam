from django.shortcuts import render, redirect

from regular_exam.my_web.forms import ProfileCreateForm


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    return render(request, 'common/dashboard.html')


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
    return render(request, 'profile/details-profile.html')
