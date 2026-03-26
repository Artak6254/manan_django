from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('contact', views.contact, name='contact'),
    path('login', views.login_view, name='login'),
    path('login_page', views.login_page, name='login_page'),
    path('register', views.register, name='register'),
    path('register_user', views.register_view, name='register_user'),
    path('forgetPass', views.forgetPass, name='forgetPass'),
    path('toggle-book/', views.toggle_book, name='toggle_book'),
    path('account', views.user_account, name='user_account'),
    path('contact', views.contact, name='contact'),
    path("category/<int:category_id>", views.category_books, name="category_books"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),

    path(
        'forgot-password/',
        auth_views.PasswordResetView.as_view(
            template_name='forgetPass.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt',
            success_url='/forgot-password/done/'
        ),
        name='password_reset'
    ),

    path(
        'forgot-password/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html',
            success_url='/reset/done/'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]