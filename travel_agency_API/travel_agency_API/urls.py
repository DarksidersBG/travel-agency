"""
URL configuration for travel_agency_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path
from travel_agency_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('travel-agency/locations', views.locations_list),
    path('travel-agency/locations/<int:id>', views.locations_detail),
    path('travel-agency/holidays', views.holidays_list),
    path('travel-agency/holidays/<int:id>', views.holidays_detail),
    path('travel-agency/reservations', views.reservations_list),
    path('travel-agency/reservations/<int:id>', views.reservations_detail)
    #path('travel-agency/locations/<int:id>', views.locations_detail1),
]
