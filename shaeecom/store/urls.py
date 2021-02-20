from django.urls import path, include
from django.contrib import admin 

from . import views

from .views import ProductList, productdetail

admin.site.site_header = "Stash Dash"
admin.site.site_title = "Welcome to the dash"
admin.site.index_title = "Welcome to the Dash"

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('services/', views.services, name="services"),
	path('about/', views.about, name="about"),
	path('portfolio/', views.portfolio, name="portfolio"),
	path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
	path('admin_dashboard_orders/', views.admin_dashboard_orders, name="admin_dashboard_orders"),
	path('admin_customer/', views.admin_customer, name="admin_customer"),
	path('admin_product/', views.admin_product, name="admin_product"),
	path('home/', views.home, name="home"),
	path('user_dashboard/', views.user_dashboard, name="user_dashboard"),
	path('user_orders/', views.user_orders, name="user_orders"),
	path('signin/', views.signin, name="signin"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('products/', ProductList.as_view()),
    path('products/<int:id>/', productdetail, name='productdetail'),
	

]