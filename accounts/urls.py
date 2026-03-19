from django.urls import path

from accounts.views import RegisterView, CustomLoginView, CustomLogoutView, ProfileDetailView, ProfileEditView, \
    ProfileDeleteView, CustomPasswordChangeView

app_name = 'accounts'
urlpatterns = [
    path('register/',RegisterView.as_view(), name = 'register'),
    path('login/',CustomLoginView.as_view(), name = 'login'),
    path('logout/',CustomLogoutView.as_view(), name = 'logout'),

    path('profile/',ProfileDetailView.as_view(), name = 'profile'),
    path('profile/edit/',ProfileEditView.as_view(), name = 'profile-edit'),
    path('profile/delete/',ProfileDeleteView.as_view(), name = 'profile-delete'),
    path('change-password/',CustomPasswordChangeView.as_view(), name = 'change-password'),
]