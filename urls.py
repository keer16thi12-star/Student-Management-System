# from django.urls import path
# from .views import home,about,contact,list_student,add_student,edit_student,delete_student
# urlpatterns=[
    # path('home/',home),
    # path('about/',about),
    # path('contact/',contact),
    # path('greet/',greet)
    # path('students/',list_student),
    # path('home/',home), 
    # path('students/',student_list,name="student_list")
    # path('students/add/', add_student),
    # path('students/edit/<int:id>/', edit_student),
    # path('students/delete/<int:id>/', delete_student)


from django.urls import path
from.views import home,about,contact,feedback,service,profile,gallery,list_students,add_students,edit_students,delete_students,students_list,delete_students,students_list,course_list
from.views import register_user,login_user,logout_user,dashboard,active_course

urlpatterns = [
    path('home/',home),
    path('about/',about),
    path('contact/',contact),
    path('feedback/',feedback),
    path('service/',service),
    path('profile/',profile),
    path('gallery/',gallery),
    path('students/',list_students),
    path('due/',course_list),
    path('students/',students_list,name="students_list"),    
    path('students/add/',add_students,name="add_students"),
    path('students/edit/<int:id>/',edit_students,name="edit_students"),
    path('students/delete/<int:id>/',delete_students,name="delete_students"),
    path('students/',register_user),
    path('login/',login_user),
    path('logout/',logout_user),
    path('dashboard/',dashboard),
    path('active/',active_course)
]
 
 
 
 
 
 
 
 
 
 



# from students import views
# urlpatterns=[
#     path('home/',views.home,name='home')
# ]