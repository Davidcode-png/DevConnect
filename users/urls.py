from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('logout/',views.logoutUser,name="logout"),
    path('register',views.registerUser,name= "register"),
    path('login/',views.loginUser,name="login"),
    path('',views.profiles,name="profiles"),
    path('profile/<str:pk>/',views.userProfile,name="user-profile"),
    path('account/',views.userAccount,name="account"),
    path('edit-account/',views.editAccount,name="edit-account"),
    path('create-skill/',views.createSkill,name="create-skill"),
    path('update-skill/<str:pk>/',views.updateSkill,name="update-skill" ),
    path('delete-skill/<str:pk>/',views.deleteSkill,name="delete-skill" )

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
