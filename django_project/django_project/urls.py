from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),  # User registration page
    path('profile/', user_views.profile, name='profile'),  # User profile page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),# Logout page
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'), #Password-reset page
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'), #Password-reset done page.
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'), #Password-reset confirm page.
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'), #Password-reset-complete page.
    path('', include('blog.urls')),  # Include blog app's URL patterns
]

# Serve static and media files in development (Only in DEBUG mode)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Static files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Media files (like profile images)
