
from django.contrib import admin
from django.urls import path
from book.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('signup', signup, name="signup"),
    path('login', login, name="login"),
    path('admin_home',admin_home,name="admin_home"),
    path('Logout',Logout,name="Logout"),
    path('user_home',user_home,name="user_home"),
    path('view_users',view_users,name="view_users"),
    path('delete_user\<int:pid>', delete_user, name="delete_user"),
    path('add_book',add_book,name="add_book"),
    path('view_book_admin',view_book_admin,name="view_book_admin"),
    path('delete_book/<int:id>',delete_book,name="delete_book"),
    path('edit_book<int:pid>',edit_book,name="edit_book"),
    path('change_bookimage/<int:id>',change_bookimage,name="change_bookimage"),
    path('change_passwordadmin', change_passwordadmin, name="change_passwordadmin"),
    path('view_feedback',view_feedback,name="view_feedback"),
    path('feedback',feedback,name="feedback"),
    path('delete_feedback/<int:id>',delete_feedback,name="delete_feedback"),
    path('view_book_user',view_book_user,name="view_book_user"),
    path('buy_now/<int:pid>',buy_now,name="buy_now"),
    path('rent_book/<int:id>',rent_book,name="rent_book"),
    path('view_booking',view_booking,name="view_booking"),
    path('cancel_booking/<int:id>', cancel_booking, name="cancel_booking"),
    path('change_passworduser',change_passworduser,name="change_passworduser"),
    path('contact',contact,name="contact"),
    path('delete_contact/<int:id>', delete_contact, name="delete_contact"),
    path('view_booking_admin',view_booking_admin,name="view_booking_admin"),
    path('delete_booking/<int:id>',delete_booking,name="delete_booking"),
    path('change_status/<int:id>', change_status, name="change_status"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
