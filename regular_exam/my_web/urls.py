from django.urls import path, include

from regular_exam.my_web.views import index, dashboard, create_fruit, details_fruit, edit_fruit, delete_fruit, \
    create_profile, edit_profile, delete_profile, details_profile

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),

    path('create/', create_fruit, name='create-fruit'),
    path('<int:pk>/details/', details_fruit, name='details-fruit'),
    path('<int:pk>/edit/', edit_fruit, name='edit-fruit'),
    path('<int:pk>/delete/', delete_fruit, name='delete-fruit'),

    path('profile/', include([
        path('create/', create_profile, name='create-profile'),
        path('edit/', edit_profile, name='edit-profile'),
        path('delete/', delete_profile, name='delete-profile'),
        path('details/', details_profile, name='details-profile'),
    ]))
)

"""
http://localhost:8000/ - index page
http://localhost:8000/dashboard/ - dashboard page

http://localhost:8000/create/ - fruit create page
http://localhost:8000/1/details/ - fruit details page
http://localhost:8000/1/edit/ - fruit edit page
http://localhost:8000/1/delete/ - fruit delete page

http://localhost:8000/profile/create/ - profile create page
http://localhost:8000/profile/details/ - profile details page
http://localhost:8000/profile/edit/ - profile edit page
http://localhost:8000/profile/delete/ - profile delete page
"""
