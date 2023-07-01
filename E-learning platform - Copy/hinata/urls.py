from django.urls import path
from . import views

urlpatterns=[
    path('',views.log_in,name="Login"),
    path('login',views.log_in,name="login"),
    path('home/',views.home,name="home"),
    path('logout', views.log_out, name='logout'),
    path('home/ml/',views.ml,name="meachin learning"),
    path('home/ds/',views.ds,name="Data science"),
    path('home/web/',views.web,name="Web development"),
    path('home/ml/mlquiz/',views.mlquiz,name="Meachin learning Quiz"),
    path('home/web/webquiz/',views.webquiz,name="Web development Quiz"),
    path('home/ds/dsquiz/',views.dsquiz,name="Data science  Quiz"),
    path('about/',views.about,name="About"),
    path('chat/',views.chat,name="CHATBOT"),
    path('courses/',views.Courses,name="Courses"),
    path('Code Editor/',views.codeeditor,name="Code"),
    #Courses 
    path('Ai/',views.Ai,name="Artifical Intelligence"),
    path('C/',views.c,name="C programming"),
    path('CPP/',views.cpp,name="c++ programming"),
    path('python/',views.python,name="Python programming"),
    path('java/',views.java,name="Java programming"),
    path('cloud/',views.cloud,name="cloud programming"),
    path('r/',views.r,name="r programming"),
    path('javascript/',views.javascript,name="javascript programming"),
]