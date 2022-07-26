from django.urls import path
from . import views
urlpatterns = [
    # Head
    # path('test/',views.loginUser,name='test'),
    path('',views.registerUser,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('login_user/',views.loginUser,name='login_user'),
    path('dashboard',views.dashboardPage,name='dashboard'),
    # Employee 
    path('e-table/',views.tablePage,name='e-table'),
    path('e_create/',views.createEmployee,name='e_create'),
    path('e_update/<str:pk>',views.updateEmployee,name='e_update'),
    path('e_delete/<str:pk>',views.deleteEmployee,name='e_delete'),
    # Product
    path('p_table/',views.productTable,name='p_table'),
    path('p_create/',views.createProduct,name='p_create'),
    path('p_update/<str:pk>',views.updateProduct,name='p_update'),
    path('p_delete/<str:pk>',views.deleteproduct,name='p_delete'),
    #  Mentor  
    path('m-table/',views.mentorTable,name='m-table'),
    path('m_creat/',views.createMentor,name='m_creat'),
    path('m_update/<str:pk>',views.updateMentor,name='m_update'),
    path('m_delete/<str:pk>',views.deleteMentor,name='m_delete'),
    # Group
    path('group_teb/',views.groupTable,name='group_teb'),
    path('group_crt/',views.createGroup,name='group_crt'),
    path('group_up/<str:pk>',views.updateGroup,name='group_up'),
    path('group_del/<str:pk>',views.deleteGroup,name='group_del'),
    # Student
    path('student_teb/',views.studentTable,name='student_teb'),
    path('student_crt/',views.createStudent,name='stuedent_crt'),
    path('student_up/<str:pk>',views.updateStudent,name='student_up'),
    path('student_del/<str:pk>',views.deleteStudent,name='student_del'),
    # Errors
    path('error_400/',views.error_400,name='error_400'),
    path('error_500/',views.error_500,name='error_500'),
]   