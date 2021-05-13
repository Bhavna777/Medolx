from django.contrib.auth import logout
from django.contrib import admin
from django.urls import path
from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name="home"),
#     path('login', views.login, name="login"),
#     path('signup', views.signup, name="signup"),
#     path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
#     path('admin_doctor', views.admin_doctor, name="admin_doctor"),
#     path('admin_view_doctor', views.admin_view_doctor, name="admin_view_doctor"),
#     path('admin_add_doctor', views.admin_add_doctor, name="admin_add_doctor"),
#     path('admin_update_doctor/<int:pk>', views.admin_update_doctor, name="admin_update_doctor"),
#     path('admin_delete_doctor/<int:pk>', views.admin_delete_doctor, name="admin_delete_doctor"),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('signin', views.signin, name="signin"),
    path('doctors', views.doctors, name="doctors"),
    path('doctor/<int:pk>', views.doctor, name="doctor"),
    path('products', views.products, name="products"),
    path('product/<int:pk>', views.product, name="product"),
    path('blogs', views.blogs, name="blogs"),
    path('blog/<int:pk>', views.blog, name="blog"),
    path('signup', views.signup, name="signup"),
    path('contact', views.contact, name="contact"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('admin_doctor', views.admin_doctor, name="admin_doctor"),
    path('admin_view_doctor', views.admin_view_doctor, name="admin_view_doctor"),
    path('admin_add_doctor', views.admin_add_doctor, name="admin_add_doctor"),
    path('admin_update_doctor/<int:pk>', views.admin_update_doctor, name="admin_update_doctor"),
    path('admin_delete_doctor/<int:pk>', views.admin_delete_doctor, name="admin_delete_doctor"),
    path('admin_patient', views.admin_patient, name="admin_patient"),
    path('admin_view_patient', views.admin_view_patient, name="admin_view_patient"),
    path('admin_add_patient', views.admin_add_patient, name="admin_add_patient"),
    path('admin_update_patient/<int:pk>', views.admin_update_patient, name="admin_update_patient"),
    path('admin_delete_patient/<int:pk>', views.admin_delete_patient, name="admin_delete_patient"),
    path('admin_add_product', views.admin_add_product, name="admin_add_product"),
    path('admin_view_product', views.admin_view_product, name="admin_view_product"),
    path('admin_update_product/<int:pk>', views.admin_update_product, name="admin_update_product"),
    path('admin_delete_product/<int:pk>', views.admin_delete_product, name="admin_delete_product"),
    path('admin_view_blog', views.admin_view_blog, name="admin_view_blog"),
    path('admin_add_blog', views.admin_add_blog, name="admin_add_blog"),
    path('admin_update_blog/<int:pk>', views.admin_update_blog, name="admin_update_blog"),
    path('admin_delete_blog/<int:pk>', views.admin_delete_blog, name="admin_delete_blog"),
    path('admin_view_message', views.admin_view_message, name="admin_view_message"),
    




    # for chat app

    #path('chat/', views.chat_view, name='chats'),
    #path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    #path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    #path('api/messages/', views.message_list, name='message-list'),






    # Logout


    path('logout/', views.logout_view, name='logout'),
]

