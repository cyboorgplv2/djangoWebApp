"""djangoWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home_view
from products.views import product_list, product_add, product_remove
from history.views import history_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('productList/', product_list),
    path('productList/Add/', product_add),
    path('remove', product_remove),
    path('history/', history_list),

]
