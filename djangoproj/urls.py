
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),
    path('', include('adminApps.urls')),
    ###### Prof#########
    path('', include('profs.urls')),
    ###### Module#######
    path('', include('modules.urls')),
    ###### Section#######
    path('', include('sections.urls')),
    ###### Schedule#######
    path('', include('schedules.urls')),
    path('', include('sessionApps.urls')),
    path('', include('classrooms.urls')),
    path('', include('students.urls')),
    path('', include('absences.urls')),
    path('', include('justifications.urls')),
    path('', include('exclusions.urls')),
    path('', include('profiles.urls')),
    path('', include('quizzy.urls')),
    # path('', include('authentication.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/auth/jwt', include('djoser.urls.jwt')),
    path('social-auth/', include('social_django.urls')),
    # (/api/auth/token/login/) to login
    # (/api/auth/token/logout/) to logout
    # /api/auth/password/reset/ to reset password
    # /api/auth/password/reset/confirm/ to confirm reset password



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
