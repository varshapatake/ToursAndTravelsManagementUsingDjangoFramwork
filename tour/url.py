from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$',views.index,name='index' ),

    url(r'^register/$',views.register,name='register' ),
    url(r'^add_register_customer_submit/$',views.add_register_customer_submit,name='add_register_customer_submit'),
    url(r'^login/$',views.login,name='login'),
    url(r'^book_package_shimala',views.book_package_shimala,name='book_package_shimala'),
    url(r'^book_package_paris', views.book_package_paris, name='book_package_paris'),
    url(r'^book_package_rome', views.book_package_rome, name='book_package_rome'),
    url(r'^book_package_london', views.book_package_london, name='book_package_london'),
    url(r'^admin',views.admin,name='admin'),
    url(r'^admin_login',views.admin_login,name="admin_login"),
    url(r'^login_check',views.login_check,name="login_check"),
    url(r'^about_us',views.about_us,name="about_us"),
    url(r'^help',views.help,name="help"),
    url(r'^logout_check', views.logout_check, name="logout_check"),
    url(r'^places', views.places, name="places"),
    url(r'^register_package', views.register_package, name="register_package"),
    url(r'^submit_register_packageinfo', views.submit_register_packageinfo, name="submit_register_packageinfo"),
    url(r'^calculate_package_cost', views.calculate_package_cost, name="calculate_package_cost"),
    url(r'^submit_payment',views.submit_payment,name="submit_payment"),
    url(r'^registration_successfull',views.registration_successfull,name="registration_successfull"),
    url(r'^register_count',views.register_count,name="register_count"),
    url(r'^profile',views.profile,name="profile"),
    url(r'^shedule',views.shedule,name="shedule"),
    url(r'^customer_package_view',views.customer_package_view,name="customer_package_view"),


]