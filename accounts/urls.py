from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
	# path('login', auth_views.LoginView.as_view(), name='login'),
	path('', views.accounts_home, name='accounts_home'),
	path('following/', views.following, name='following'),
	path('followers/', views.followers, name='followers'),
	path('logout', auth_views.LogoutView.as_view(), name='logout'),
	path('login', views.login_view, name='login'),
	path('register/', views.register, name='register'),
	path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('accounts:password_change_done')), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'),
	path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
	path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

	

	path('<str:username>/', views.profile_view, name='profile'),
	path('<str:username>/edit', views.edit_profile_view, name='edit_profile'),
	path('<str:username>/follow', views.follow_view, name='follow'),
	path('<str:username>/unfollow', views.unfollow_view, name='unfollow'),
	# path

	# path('reset_password/', auth_views)
]

