from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.sign_in, name="login"),
    path("gallery/", views.gallery, name="gallery"),
    path("logout", views.sign_out, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
        "projects/",
        include(
            [
                path("", views.project_list, name="project_list"),
                path("show/<int:projectID>", views.project_show, name="project_show"),
                path("create/", views.project_create, name="project_create"),
                path(
                    "delete/<int:projectID>",
                    views.project_delete,
                    name="project_delete",
                ),
                path("edit/<int:projectID>", views.project_edit, name="project_edit"),
            ]
        ),
    ),
    path(
        "inbox",
        include(
            [
                path("", views.inbox_list, name="inbox_list"),
                path("show/<int:inboxID>", views.inbox_show, name="inbox_show"),
                path('create', views.inbox_create, name="inbox_create"),
                path('delete/<int:inboxID>', views.inbox_destroy, name="inbox_destroy")
            ]
        ),
    ),
    
    path(
        'appointment', include([
            path('', views.appointment_list, name="appointment_list"),
            path('show/<int:appointmentID>', views.appointment_show, name="appointment_show"),
            path('create', views.appointment_create, name="appointment_create")
        ])
    )
   
]
